# -*- coding: utf-8 -*-
import csv
import os
import re
import urllib2
import urllib

from bs4 import BeautifulSoup

path = './dataset'
dataReader = csv.reader(open('resources/company_list', 'rt'))

for row in dataReader:
    filename = row[0] + ".txt"
    if not os.path.isfile(filename):
        opener = urllib2.build_opener()
        opener.addheaders = [('User-agent', 'Mozilla/5.0')]

        if not row[2]:
            url_site = "https://www.google.co.jp/search?num=3&q=" + urllib.parse.quote(re.sub("株式会社", "", row[1]))
            html = opener.open(url_site)
            bs_site = BeautifulSoup(html.read(), "lxml")
            if not bs_site.find_all("div", {"id": "res"})[0].get_text():
                continue
            elif len(
                    re.findall("wiki", bs_site.find_all("div", {"id": "res"})[0].cite.get_text())) == 0:
                if len(re.findall("/[^\./]*(ja)|(jp)[^\./]*$",
                                  bs_site.find_all("div", {"id": "res"})[0].cite.get_text())) > 0:
                    url_company = bs_site.find("div", {"id": "res"}).cite.get_text()
                else:
                    url_company = re.sub("(\.[a-z]+)/.+$", "\\1", bs_site.find("div", {"id": "res"}).cite.get_text())
            else:
                url_company = re.sub("/[^\.]+", "", bs_site.find("div", {"id": "res"}).find_all("cite")[1].get_text())
        else:
            url_company = row[2]

        url_result = "https://www.google.co.jp/search?num=30&lr=lang_ja&q=site:" + urllib.parse.quote(url_company)
        html = opener.open(url_result)
        bs_result = BeautifulSoup(html.read(), "lxml")
        if len(bs_result.find_all("span", {"class": "st"})) > 1:
            result = "\n".join(
                [re.sub("['\n\.]", "", x.get_text()) for x in bs_result.find_all("span", {"class": "st"})])
        else:
            continue

        # 結果の書き込み
        fw = open(path + "/" + filename, 'w', encoding='utf-8')
        fw.write(result)
        fw.close()
