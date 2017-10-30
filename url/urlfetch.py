import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://www.nigerian-prince.ru/"
    res = urllib.request.urlopen(url)
    html = res.readlines()
    soup = BeautifulSoup(html)
    text = soup.get_text()
    print(text)
