# -*- coding: utf-8 -*-
import pycurl

if __name__ == '__main__':
    half1 = ""
    half2 = ""

    with open('alertHalf1') as f:
        for l in f:
            half1 += l.rstrip()

    with open('alertHalf2') as f:
        for l in f:
            half2 += l.rstrip()

    name = '{"name": "kvset'

    command = '                        "command": "kv_set -table fuga -key meta.msg -value meta.msg",'

    js = []

    for i in range(1, 99):
        command = command.replace('fuga', 'fugaa')
        js.append(((name + str(i)) + half1 + command + half2).replace('               ', ''))

    for j in js:
        # print(j)
        curl = pycurl.Curl()
        curl.setopt(pycurl.URL, 'http://admin:admin@xsiem01:8090/v1/rules')
        curl.setopt(pycurl.POSTFIELDS, j)
        curl.setopt(pycurl.HTTPHEADER, ['Content-Type: application/json'])
        curl.perform()
