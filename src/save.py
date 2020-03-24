import os
from urllib.request import urlretrieve
import psycopg2

conn = psycopg2.connect(host='ec2-54-247-79-178.eu-west-1.compute.amazonaws.com',
                        user='jtiewymsqrsflb',
                        password='25c2468e8a3af8a1a1bd12d7eebb6ad0e6f0cc243f1c1430993d40c210b667c9',
                        dbname='dcgnunfjhhkmdf')


def save(name, description, geo_coordinates, full_address, words, photo_url):
    cursor = conn.cursor()
    sql = "insert into attractions (name, description, geo_coordinates, full_address, word_list, photo_path) " \
          "values ('" + name + "', '" + description + "', '" + geo_coordinates + "', '" + full_address + "', '" + \
          str(words).replace('[', '').replace(']', '').replace('\'', '') + "', '" + photo_url + "')"
    cursor.execute(sql)
    conn.commit()


def save_photo(image_link, path_save_dir):
    path = path_save_dir + '/img.jpg'
    urlretrieve(image_link, path)
    path = os.path.abspath(path_save_dir + '/img.jpg')
    return path
