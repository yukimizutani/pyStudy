import urllib
from bs4 import BeautifulSoup

url = 'https://theriver.jp/ps4-spm-uk/'

if __name__ == '__main__':
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
            if not li == '':
                print(str(li))
