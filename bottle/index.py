# -*- coding:utf-8 -*-

from bottle import Bottle, run, get, post, request, static_file
from bottle import TEMPLATE_PATH, jinja2_template as template
from study_jinja2.basics import include, extend
import os
from collections import OrderedDict

TEMPLATE_PATH.append("./template")
app = Bottle()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


# static file CSS
@app.route('/static/css/<filename:path>')
def static_css(filename):
    return static_file(filename, root=STATIC_DIR + "/css")


@app.route('/static/images/<filename:path>')
def static_images(filename):
    return static_file(filename, root=STATIC_DIR + "/images")


def get_image_files():
    root_dir = "/home/yuki/PycharmProjects/pyStudy/bottle/static/images"
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
    return OrderedDict(sorted(file_dict.items(), key=lambda x: x[0]))


@app.route('/', method='GET')
def root():
    content_type = request.query.contentType
    content_type = "top" if content_type is None else content_type
    if content_type == 'top':
        child_elem = template('top_content/top_content.tpl')
    elif content_type == 'myPage':
        child_elem = template('mypage_content/mypage_content.tpl')
    elif content_type == 'code':
        child_elem = template('code_content/code_content.tpl', codeDict=get_image_files())
    elif content_type == 'trade':
        child_elem = template('trade_content/trade_content.tpl')
    elif content_type == 'shop':
        child_elem = template('shop_content/shop_content.tpl')
    else:
        child_elem = template('top_content/top_content.tpl')
    return template('base/child.tpl', contentType=content_type, childElem=child_elem)


@app.route('/tesuto')
def tesuto():
    return include.include_template()


@app.route('/hello/<name>')
def hello(name):
    return template('hello.j2', name=name)


@app.route('/date/<month:re:[a-z]+>/<day:int>/<path:path>')
def date(month, day, path):
    return "{month}/{day} {path}".format(month=month, day=day, path=path)


@app.route('/login', method='GET')
def login():
    username = request.query.get('user')
    password = request.query.get('pass')

    # GETで何も渡されていない時はusername,passwordに何も入れない
    username = "" if username is None else username
    password = "" if password is None else password

    return template('login/login.html', username=username, password=password)


@app.route('/login', method='POST')  # or @post('/post')
def do_login():
    username = request.forms.get('username')
    password = request.forms.get('password')

    return template("{username} {password}".format(username=username, password=password))


@app.route('', method='POST')
def save_items():
    dirname = request.forms.get('dir')
    item = request.forms.get('item')

    ## do save


if __name__ == "__main__":
    run(app=app, host="localhost", quiet=False, reloader=True, debug=True)
