import urllib.request, urllib
from bs4 import BeautifulSoup
import time
from selenium import webdriver
import re
import pandas as pd

rss_urls = []

for i in range(17):
    print("Page:"+str(i))
    page = i+1
    url = "https://official.ameba.jp/rankings/total?pageNo="+str(page)
    driver = webdriver.PhantomJS()
    driver.get(url)
    soup = BeautifulSoup(driver.page_source, "html5lib")
    cites = soup.find_all("a", class_="ranking-list-title-link")
    for cite in cites:
        rss_urls.append(re.sub(r'https://ameblo.jp/(.+)/', r'http://rssblog.ameba.jp/\1/rss20.xml', cite['href']))

rss_urls_df = pd.DataFrame(rss_urls, columns=["rss"])
rss_urls_df.to_csv("rss_data_ameblo.csv", index=False)

texts = []
for rss_url in rss_urls:
    text = ""
    try:
        req = urllib.request.Request(rss_url)
        xml = urllib.request.urlopen(req)
        soup = BeautifulSoup(xml, "lxml-xml")
        descs = soup.find_all("description")
        for desc in descs:
            tmp = re.sub(r'[a-zA-Z0-9<>\-_\./=\"\':]',"", desc.text)
            tmp = re.sub(r'続きを[見み]る', "", tmp)
            tmp = re.sub(r'『著作権保護のため、記事の一部のみ表示されております。』', "", tmp)
            tmp = re.sub(r'[ 　]', "", tmp)
            tmp = re.sub(r'\n', "", tmp)
            text = text + tmp
    except:
        pass
    texts.append(text)

texts_df = pd.DataFrame(texts, columns=["text"])

out = pd.DataFrame()
out["url"] = rss_urls_df
out["text"] = texts_df
out.to_csv("ameblo_tests.csv")