from aaaabottle import Bottle, run, route, request, response

app = Bottle()


@app.route('/counter')
def counter():
    count = int(request.cookies.get('counter', '0'))
    count += 1
    response.set_cookie('counter', str(count), max_age=2678400)  # 最大３１日有効
    return 'You visited this page %d times' % count


if __name__ == "__main__":
    run(app=app, host="0.0.0.0", port='8080', debug=True)
