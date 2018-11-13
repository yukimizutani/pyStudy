import urllib.request, urllib.error
from bs4 import BeautifulSoup

url = 'https://news.cardmics.com/entry/amex-hakko-speed/'


def show_text(soup):
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text().split('\n')
    for li in text:
        if not li == '':
            print(str(li))


def show_raw(soup):
    print(soup)


if __name__ == '__main__':
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:47.0) Gecko/20100101 Firefox/47.0",
        }
        request = urllib.request.Request(url=url, headers=headers)
        res = urllib.request.urlopen(request)
    except urllib.error.URLError as e:
        print(e.reason)
        pass
    else:
        html = res.read()
        soup = BeautifulSoup(html)
        show_text(soup)
