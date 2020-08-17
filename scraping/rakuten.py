# -*- coding: utf-8 -*-

import urllib.request, urllib.error
from bs4 import BeautifulSoup
from urllib.parse import urlparse

japanese = '恐怖の泉'
url_pre = 'https://' + urllib.parse.quote(japanese) + '.com/kaidan/'
url_post = 'wa.html'


def show_text(soup1):
    # remove scripts
    for script in soup1(["script", "style"]):
        script.decompose()
    text = soup1.get_text().replace('。', '。\n').split('\n')
    for li in text:
        if '前の話' in li:
            break
        else:
            print(li)


def show_raw(soup2):
    print(soup2)


if __name__ == '__main__':
    for i in range(200, 299):
        url = 'https://www.rakuten.co.jp/'
        try:
            headers = {
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
            }
            request = urllib.request.Request(url=url, headers=headers)
            request.add_header('Host', request.host.encode('idna'))
            res = urllib.request.urlopen(request)
        except urllib.error.URLError as e:
            print(e.reason, e.strerror)
            pass
        else:
            html = res.read()
            soup = BeautifulSoup(html, features="html.parser")
            show_raw(soup)
        print('')
