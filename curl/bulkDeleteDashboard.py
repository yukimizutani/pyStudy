import pycurl

if __name__ == '__main__':
    curl = pycurl.Curl()
    curl.setopt(pycurl.URL, 'http://admin:admin@xsiem01:8090/v1/ui/dashboards?bulk=false')
    curl.setopt(curl.DELETE, True)
    curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
    curl.perform()
