import re
import requests
from bs4 import BeautifulSoup

site = 'https://prichan.jp/items/details/70000.html'
base = 'https://prichan.jp'


def scavenge():
    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_tags = [img for img in img_tags if 'lazy' in str(img)]

    urls = [img['data-src'] for img in img_tags if img['data-src'] is not None]

    for url in urls:
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        with open(filename.group(1), 'wb') as f:
            if 'http' not in url:
                # sometimes an image source can be relative
                # if it is provide the base url which also happens
                # to be the site variable atm.
                url = '{}{}'.format(base, url)
            response = requests.get(url)
            f.write(response.content)


if __name__ == '__main__':
    scavenge()
