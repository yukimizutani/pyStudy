import urllib.request
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = "https://closedsearch.auctions.yahoo.co.jp/"
    res = urllib.request.urlopen(url)
    html = res.read()
    soup = BeautifulSoup(html, 'lxml')
    text = soup.get_text()
    print(text)
