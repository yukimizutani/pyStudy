import urllib.request
from bs4 import BeautifulSoup


def poke_main(page):
    url = "http://www.jisaka.com?p={}".format(page)
    try:
        res = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        pass
    else:
        html = res.read()
        soup = BeautifulSoup(html, 'lxml')
        for script in soup(["script", "style"]):
            script.decompose()
        str_soup = soup.prettify()
        for line in str_soup.split('\n'):
            if 'content' not in vars():
                content = False
            if '<!-- 記事　はじまり -->' in line:
                content = True
            if content:
                if 'article' not in vars():
                    article = False
                if article:
                    print(line)
                    article = False
                if 'itemprop="url"' in line:
                    article = True
                    print(line)
            if '<!-- /記事 ここまで-->' in line:
                content = False


def poke_article(doc_id):
    url = 'http://www.jisaka.com/archives/{}.html'.format(doc_id)
    try:
        res = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        pass
    else:
        html = res.read()
        soup = BeautifulSoup(html, 'lxml')
        for script in soup(["script", "style"]):
            script.decompose()
        text = soup.get_text().split('\n')
        for li in text:
            if '名無し' not in li and 'お送りします' not in li and not li == '':
                print(str(li))


if __name__ == '__main__':
    for p in range(4, 10):
        poke_main(p)
    poke_article(27693956)
