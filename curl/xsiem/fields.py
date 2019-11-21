from io import BytesIO
import pycurl, json

pre = '{\"internalName\":\"'
mid = '\",\"displayName\":\"'
post = '\"}'


def delete_all():
    buffer = BytesIO()

    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER, ["Content-type: application/json"])
    c.setopt(pycurl.USERPWD, 'admin:admin')
    c.setopt(pycurl.PROXY, 'localhost')
    c.setopt(pycurl.PROXYPORT, 8090)
    c.setopt(c.URL, 'http://admin:admin@localhost:8090/v1/fields')
    c.setopt(c.WRITEFUNCTION, buffer.write)
    c.perform()
    c.close()

    body = buffer.getvalue().decode('UTF-8')
    js = json.loads(body)

    delete_request = pycurl.Curl()
    delete_request.setopt(pycurl.HTTPHEADER, ["Content-type: application/json"])
    delete_request.setopt(pycurl.USERPWD, 'admin:admin')
    delete_request.setopt(pycurl.PROXY, 'localhost')
    delete_request.setopt(pycurl.PROXYPORT, 8090)
    delete_request.setopt(pycurl.CUSTOMREQUEST, 'DELETE')

    for res in js['resources']:
        delete_request.setopt(delete_request.URL,
                              'http://admin:admin@xsiem02.dev.infoscience.co.jp:8090/v1/fields/' + str(res['resource']['id']))
        delete_request.perform()
    delete_request.close()


def register_1000():
    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER, ["Content-type: application/json"])
    c.setopt(pycurl.USERPWD, 'admin:admin')
    c.setopt(pycurl.PROXY, 'localhost')
    c.setopt(pycurl.PROXYPORT, 8090)
    c.setopt(c.URL, 'http://admin:admin@localhost:8090/v1/fields')
    for i in range(0, 1000):
        c.setopt(pycurl.POSTFIELDS, pre + str(i) + mid + str(i) + post)
        c.perform()
    c.close()


if __name__ == '__main__':
    delete_all()
    # register_1000()
