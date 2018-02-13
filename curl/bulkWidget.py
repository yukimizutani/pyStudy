import pycurl

dashboard = '{"name": "tesutoo","widgets": ['
widget = '{"name": "aaa","color": "#005BAB","posX": 0,"posY": 0,"width": 2,"height": 1,"resourceId": 0,"settings": {}}'
js = []

if __name__ == '__main__':
    for i in range(0, 110):
        js.append(widget)

    json = dashboard + ','.join(js) + ']}'

    # print(j)
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, 'http://admin:admin@xsiem01:8090/v1/ui/dashboards')
    curl.setopt(pycurl.POSTFIELDS, json)
    curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    curl.perform()
