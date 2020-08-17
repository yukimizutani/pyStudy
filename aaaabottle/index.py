# -*- coding:utf-8 -*-

from bottle import Bottle, run, get, post, request, static_file, redirect
from bottle import TEMPLATE_PATH, jinja2_template as template
import os
from collections import OrderedDict
import sqlite3
import json

TEMPLATE_PATH.append("./template")
app = Bottle()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

conn = sqlite3.connect('code.db')


# static file CSS
@app.route('/static/css/<filename:path>')
def static_css(filename):
    return static_file(filename, root=STATIC_DIR + "/css")


@app.route('/static/images/<filename:path>')
def static_images(filename):
    return static_file(filename, root=STATIC_DIR + "/images")


def get_image_files(return_dict=True):
    root_dir = STATIC_DIR + "/images"
    file_set = set()
    file_dict = {}

    for dir_, _, files in os.walk(root_dir):
        for fileName in files:
            rel_dir = os.path.relpath(dir_, root_dir)
            rel_file = os.path.join(rel_dir, fileName)
            file_set.add(rel_file)

    if return_dict:
        for elm in file_set:
            key = str(elm).split('/')
            if key[0] in file_dict:
                file_dict[key[0]].append(key[1])
            else:
                file_dict[key[0]] = [key[1]]
        for key in file_dict.keys():
            file_dict[key].sort()
        return OrderedDict(sorted(file_dict.items(), key=lambda x: x[0]))


def load_db(user, password):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM stocks WHERE user=?", (user,))
        record = c.fetchone()
        if record:
            print("Found!")
            return json.loads(record[1])
        else:
            print("Not found...")
            c.execute("SELECT * FROM stocks WHERE user=?", ("all",))
            all_code = json.loads(c.fetchone()[1])
            c.execute("INSERT INTO stocks VALUES (?,?,?)", (user, json.dumps(all_code), password))
            return all_code


def update_db(user, owned_codes, password):
    with conn:
        c = conn.cursor()
        c.execute("SELECT * FROM stocks WHERE user=?", (user,))
        rec = c.fetchone()
        if rec:
            print("Found!")
            old_items = json.loads(rec[1])
            for own_code in owned_codes:
                own_code = own_code.replace('static/images/', '').split('/')
                if own_code[0] in old_items.keys():
                    if own_code[1] in old_items[own_code[0]]:
                        old_items[own_code[0]].remove(own_code[1])
            c.execute('UPDATE stocks SET list = ? WHERE user = ?', (json.dumps(old_items), user))
        else:
            print("Not found...")
            c.execute("SELECT * FROM stocks WHERE user=?", ("all",))
            all_code = json.loads(c.fetchone()[1])
            c.execute("INSERT INTO stocks VALUES (?,?,?)", (user, all_code, password))


def reset_db(user, codes):
    with conn:
        c = conn.cursor()
        if codes is None:
            c.execute("SELECT * FROM stocks WHERE user=?", ("all",))
            code = json.loads(c.fetchone()[1])
        else:
            code = {}
            for own_code in codes:
                own_code = own_code.replace('static/images/', '').split('/')
                if own_code[0] in code:
                    code[own_code[0]].append(own_code[1])
                else:
                    code[own_code[0]] = [own_code[1]]
        c.execute('UPDATE stocks SET list = ? WHERE user = ?', (json.dumps(code), user))


@app.route('/my_code', method='POST')
def root():
    content_type = request.query.contentType
    usr = request.forms.get('username')
    password = request.forms.get('password')
    action = request.forms.get('action')
    # check credential
    if action == 'login':
        if usr == '' or password == '':
            print("Empty")
        else:
            with conn:
                c = conn.cursor()
                c.execute("SELECT * FROM stocks WHERE user=? AND password=?", (usr, password))
                rec = c.fetchone()
                if rec:
                    print("Found!")
                    content_type = "code" if content_type is '' else content_type
                    if content_type == 'top':
                        child_elem = template('top_content/top_content.tpl')
                    elif content_type == 'myPage':
                        child_elem = template('mypage_content/mypage_content.tpl')
                    elif content_type == 'code':
                        child_elem = template('code_content/code_content.tpl', codeDict=load_db(usr, password))
                    elif content_type == 'trade':
                        child_elem = template('trade_content/trade_content.tpl')
                    elif content_type == 'shop':
                        child_elem = template('shop_content/shop_content.tpl')
                    else:
                        child_elem = template('top_content/top_content.tpl')
                    return template('base/child.tpl', contentType=content_type, childElem=child_elem)
                else:
                    print("Not found!")
                    return redirect('/')
    elif action == 'register':
        if usr == '' or password == '':
            print("Empty")
        else:
            print("register")
            with conn:
                c = conn.cursor()
                c.execute("SELECT * FROM stocks WHERE user=?", (usr,))
                rec = c.fetchone()
                if rec:
                    print("Found!")
                    return template('Att.2020-04_30_水谷祐貴.csv/create_new.html', message="そのユーザー名は使用できません")
                else:
                    child_elem = template('code_content/code_content.tpl', codeDict=load_db(usr, password))
                    return template('base/child.tpl', contentType='code', childElem=child_elem)
    else:
        print("what")


@app.route('/hello/<name>')
def hello(name):
    return template('hello.j2', name=name)


@app.route('/date/<month:re:[a-z]+>/<day:int>/<path:path>')
def date(month, day, path):
    return "{month}/{day} {path}".format(month=month, day=day, path=path)


@app.route('/', method='GET')
def login():
    username = request.query.get('user')
    password = request.query.get('pass')

    # GETで何も渡されていない時はusername,passwordに何も入れない
    username = "" if username is None else username
    password = "" if password is None else password

    return template('login/login.html', username=username, password=password)


@app.route('/create_new', method='POST')
def create_new():
    return template('Att.2020-04_30_水谷祐貴.csv/create_new.html')


@app.route('/save_items', method='POST')
def save_items():
    items = request.json
    user = 'admin'
    password = 'admin'

    # do save
    update_db(user, items, password)

    return "Updated"


@app.route('/reset_items', method='POST')
def reset_items():
    user = request.forms.get('usr')
    codes = request.forms.get('code')

    # do reset
    reset_db(user, codes)

    return "hello"


@app.route('/initialize', method='POST')
def initialize():
    user = request.forms.get('usr')

    # do reset
    reset_db(user, None)

    return "hello"


if __name__ == "__main__":
    run(app=app, host="localhost", port=8080, quiet=False, reloader=True, debug=True)
