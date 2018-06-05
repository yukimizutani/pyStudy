# -*- coding:utf-8 -*-

from bottle import Bottle, run, get, post, request, static_file
from bottle import TEMPLATE_PATH, jinja2_template as template
from study_jinja2.basics import include, extend
import os

TEMPLATE_PATH.append("./template")
app = Bottle()

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')


# static file CSS
@app.route('/static/css/<filename:path>')
def static_css(filename):
    return static_file(filename, root=STATIC_DIR + "/css")


@app.route('/')
def root():
    return template('base/child.tpl')


@app.route('/content/top_content')
def top_content():
    return template('smthsmth')


@app.route('/tesuto')
def tesuto():
    return include.include_template()


@app.route('/hello/<name>')
def hello(name):
    return template('hello.j2', name=name)


@app.route('/date/<month:re:[a-z]+>/<day:int>/<path:path>')
def date(month, day, path):
    return "{month}/{day} {path}".format(month=month, day=day, path=path)


@app.route('/login', method='GET')  # or @get('/login')
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

    return "{username} {password}".format(username=username, password=password)


if __name__ == "__main__":
    run(app=app, host="0.0.0.0", quiet=False, reloader=True, debug=True)
