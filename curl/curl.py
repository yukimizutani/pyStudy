import pycurl, json

if __name__ == '__main__':
    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER, ["Content-type: application/json"])
    c.setopt(pycurl.USERPWD, 'admin:admin')
    c.setopt(pycurl.PROXY, 'xsiem01')
    c.setopt(pycurl.PROXYPORT, 8090)
    c.setopt(c.URL, 'http:/v1/command/admin/taskmanager/2')
    res = c.perform()
    print(str(res))

    js = json.loads(str(res))

    # print(js)

