def find_geo_coordinates(browser):
    return browser.find_element_by_class_name('mw-kartographer-maplink').text.strip()


def find_full_address(browser):
    plain_list = browser.find_elements_by_class_name("plainlist")
    text = ""
    for i in range(len(plain_list)):
        title = plain_list[i].text.lower()
        if title == "адрес" or title == 'город' or title == 'район':
            text += plain_list[i + 1].text + " "
    if text != "":
        return text.strip()
    return "Адрес не найден"


def find_word_list(browser):
    bad_words = ["от", "до", "на", "по", "со", "из", "над", "под", "при", "про", "без", "ради", "близ", "перед",
                 "около", "через", "вдоль", "после", "кроме", "сквозь", "вроде", "вследствие", "благодаря",
                 "вопреки", "согласно", "навсречу", "не", "для", "был", "было", "что", "были", "его", "как", "была",
                 "их", "также", "за", "более", "или", "за", "но"]
    text = browser.find_element_by_class_name('mw-parser-output').text
    word_list = []
    for word in text.split():
        clear_word = ''
        for letter in word:
            if letter.isalpha():
                clear_word += letter.lower()
        if len(clear_word) > 1 and clear_word not in bad_words:
            word_list.append(clear_word)
    return word_list


def find_image_link(browser):
    infobox_images = browser.find_elements_by_class_name('infobox-image')
    if len(infobox_images) == 0:
        return 'Фото не найдено'
    infobox_image = infobox_images[0]
    images = infobox_image.find_elements_by_tag_name('img')
    image_links = []
    for image in images:
        image_link = image.get_attribute('src')
        image_links.append(image_link)
    return image_links[0]


def find_description(browser):
    body_content = browser.find_elements_by_class_name('mw-parser-output')[0]
    paragraphs = body_content.find_elements_by_tag_name('p')
    description = ""
    if paragraphs[0] is not None and paragraphs[0].text.strip() != "" and paragraphs[0].text.strip() != "\n":
        description += paragraphs[0].text
    if paragraphs[1] is not None and paragraphs[1].text.strip() != "" and paragraphs[0].text.strip() != "\n":
        description += '\n' + paragraphs[1].text
    if paragraphs[2] is not None and paragraphs[2].text.strip() != "" and paragraphs[0].text.strip() != "\n":
        description += '\n' + paragraphs[2].text
    return description.strip()
