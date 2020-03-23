from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from collections import Counter
import os
import sys

from src.find import find_description, find_image_link, find_word_list, find_geo_coordinates, find_full_address
from src.save import save, save_photo


def open_browser(path_webdriver):
    try:
        browser = webdriver.Chrome(path_webdriver)
        browser.implicitly_wait(6)
        return browser
    except WebDriverException as e:
        print("Указан не верный путь к webdriver! Исправите его и попробуйте снова!")
        exit(1)


def parse(path_webdriver, path_main_dir, url_location):
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

        path_save_dir = path_main_dir + '/' + name
        try:
            os.mkdir(path_save_dir)
        except:
            pass
        # сохранение
        photo_path = save_photo(image_link, path_save_dir)
        save(name, description, geo_coordinates, full_address, Counter(word_list).most_common(30), photo_path)

    except Exception as e:
        print('Ошибка в программе, обратитесь к разработчику.')
        print(e)
    finally:
        browser.quit()


def main(url_location):
    path_webdriver = 'chromedriver.exe'
    path_main_dir = '../attractions'
    try:
        os.mkdir(path_main_dir)
    except:
        pass
    parse(path_webdriver, path_main_dir, url_location)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Ожидался url страницы')
        exit(1)
    main(sys.argv[1])
