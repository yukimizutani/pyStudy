import pycurl


name = '{"name": "widget'
js = []


if __name__ == '__main__':
    for i in range(99, 10000):
        js.append((name + str(i) + '\"}'))

    for j in js:
        # print(j)
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, 'http://admin:admin@xsiem01:8090/v1/ui/dashboards')
        curl.setopt(pycurl.POSTFIELDS, j)
        curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        curl.perform()
