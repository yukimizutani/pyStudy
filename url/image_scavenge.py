import re

import os
import requests
from bs4 import BeautifulSoup

site = 'https://prichan.jp/items/2nd.html'
base = 'https://prichan.jp'


def see_url():
    response = requests.get(site)
    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    for tag in img_tags:
        print(tag)


def scavenge():
    response = requests.get(site)

    soup = BeautifulSoup(response.text, 'html.parser')
    img_tags = soup.find_all('img')
    img_tags = [img for img in img_tags if 'lazy' in str(img)]

    urls = [img['data-src'] for img in img_tags if img['data-src'] is not None]

    for url in urls:
        has_outfits = False
        if 'outfits' in url:
            has_outfits = True
            image_group = re.search(r'outfits/(.+)[.](jpg|gif|png)$', url)
            if image_group is not None:
                dir_name = image_group.group(1)
            else:
                dir_name = '2-20'
        filename = re.search(r'/([\w_-]+[.](jpg|gif|png))$', url)
        if filename is not None and 'dir_name' in locals() and not has_outfits:
            relative_path = dir_name + '/' + filename.group(1)
            if not os.path.exists(os.path.dirname(relative_path)):
                try:
                    os.makedirs(os.path.dirname(relative_path))
                except OSError:  # Guard against race condition
                    raise
            with open(relative_path, 'wb') as f:
                if 'http' not in url:
                    # sometimes an image source can be relative
                    # if it is provide the base url which also happens
                    # to be the site variable atm.
                    url = '{}{}'.format(base, url)
                response = requests.get(url)
                f.write(response.content)


if __name__ == '__main__':
    scavenge()
    # see_url()
