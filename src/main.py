import sys
from collections import Counter

from selenium import webdriver
from selenium.common.exceptions import WebDriverException

from src.find import find_description, find_image_link, find_word_list, find_geo_coordinates, find_full_address
from src.save import save


def open_browser(path_webdriver):
    try:
        browser = webdriver.Chrome(path_webdriver)
        browser.implicitly_wait(6)
        return browser
    except WebDriverException as e:
        print("Указан не верный путь к webdriver! Исправите его и попробуйте снова!")
        exit(1)


def parse(path_webdriver, url_location):
    browser = open_browser(path_webdriver)
    try:
        browser.get(url_location)
        name = browser.find_element_by_id('firstHeading').text

        # поиск
        description = find_description(browser)
        image_link = find_image_link(browser)
        word_list = find_word_list(browser)
        geo_coordinates = find_geo_coordinates(browser)
        full_address = find_full_address(browser)

        # сохранение
        save(name, description, geo_coordinates, full_address, Counter(word_list).most_common(30), image_link)

        print('Достопримечательность "'+ name + '" успешно сохранена')
    except Exception as e:
        if 'duplicate key value violates unique constraint "attractions_name_uindex"' in str(e):
            print('Достопримечательность с таким названием уже есть в базе')
        else:
            print('Ошибка в программе, обратитесь к разработчику.')
            print(str(e))
    finally:
        browser.quit()


def main(url_location):
    path_webdriver = 'chromedriver.exe'
    parse(path_webdriver, url_location)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Ожидался url страницы')
        exit(1)
    main(sys.argv[1])
