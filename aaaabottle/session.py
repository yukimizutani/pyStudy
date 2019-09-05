from aaaabottle import Bottle, run, route, request, response
from beaker.middleware import SessionMiddleware

session_opts = {
    'session.type': 'file',
    'session.cookie_expires': 300,
    'session.data_dir': './data',
    'session.auto': True
}

app = Bottle()
apps = SessionMiddleware(app, session_opts)


@app.route('/count')
def counter():
    count = request.environ.get('beaker.session')
    count['times'] = count.get('times', 0) + 1
    count.save()
    return 'You visited this page %d times' % count['times']


if __name__ == "__main__":
    run(app=apps, host="0.0.0.0", port='8080', debug=True)
