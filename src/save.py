from urllib.request import urlretrieve


def save_photo(image_link, path_save_dir):
    urlretrieve(image_link, path_save_dir + '/img.jpg')


def save_description(text, path_save_dir):
    with open(path_save_dir + '/description.txt', 'w', encoding='utf8') as f:
        f.write(text)


def save_geo_coordinates(text, path_save_dir):
    with open(path_save_dir + '/geo_coordinates.txt', 'w', encoding='utf8') as f:
        f.write(text)


def save_full_address(text, path_save_dir):
    with open(path_save_dir + '/full_address.txt', 'w', encoding='utf8') as f:
        f.write(text)


def save_word_list(words, path_save_dir):
    with open(path_save_dir + '/word_list.txt', 'w', encoding='utf8') as f:
        for word in words:
            f.write(str(word) + "\n")
