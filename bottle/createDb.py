import os
import sqlite3
import json
from collections import OrderedDict
import base64

db_filename = 'code.db'
db_is_new = not os.path.exists(db_filename)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


def get_image_files():
    root_dir = STATIC_DIR + "/images"
    file_set = set()
    file_dict = {}

    for dir_, _, files in os.walk(root_dir):
        for fileName in files:
            rel_dir = os.path.relpath(dir_, root_dir)
            rel_file = os.path.join(rel_dir, fileName)
            file_set.add(rel_file)

    for elm in file_set:
        key = str(elm).split('/')
        if key[0] in file_dict:
            file_dict[key[0]].append(key[1])
        else:
            file_dict[key[0]] = [key[1]]
    for key in file_dict.keys():
        file_dict[key].sort()
    return OrderedDict(sorted(file_dict.items(), key=lambda x: x[0]))


def do_create():
    with sqlite3.connect(db_filename) as conn:
        c = conn.cursor()
        if db_is_new:
            print('Creating schema')

            c.execute('''CREATE TABLE stocks
                         (user text PRIMARY KEY, list  text, password text)''')
            c.execute("INSERT INTO stocks VALUES (?,?,?)",
                      ('all', json.dumps(get_image_files()), base64.b64encode(str.encode('all'))))
            conn.commit()
        else:
            print('Already there')


def check():
    with sqlite3.connect(db_filename) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM stocks')
        for usr, code, passwd in c.fetchall():
            print(usr, code, passwd)


def update():
    all_images = get_image_files()

    with sqlite3.connect(db_filename) as conn:
        c = conn.cursor()
        c.execute('SELECT * FROM stocks')
        for usr, code, passwd in c.fetchall():
            to_update = {}
            code = json.loads(code)
            for dir_name in all_images:
                if dir_name not in code.keys():
                    to_update[dir_name] = all_images[dir_name]
            to_update.update(code)
            print(usr, to_update, passwd)
            c.execute('UPDATE stocks SET list = ? WHERE user = ? AND password = ?',
                      (json.dumps(to_update), 'all', passwd))


if __name__ == '__main__':
    do_create()
    check()
    # update()
