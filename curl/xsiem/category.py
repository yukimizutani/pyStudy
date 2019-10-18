import pycurl, json

pre = '{\"name\":\"test'
post = '\",\"type\":\"simple\"}'

requests = []

for i in range(0, 10):
    requests.append(pre + str(i) + post)

if __name__ == '__main__':
    c = pycurl.Curl()
    c.setopt(pycurl.HTTPHEADER, ["Content-type: application/json"])
    c.setopt(pycurl.USERPWD, 'admin:admin')
    c.setopt(pycurl.PROXY, 'localhost')
    c.setopt(pycurl.PROXYPORT, 8090)
    c.setopt(c.URL, 'http://admin:admin@localhost:8090/v1/category')
    for j in requests:
        c.setopt(pycurl.POSTFIELDS, j)
        res = c.perform()
        print(str(res))

    # js = json.loads(str(res))
    #
    # print(js)
