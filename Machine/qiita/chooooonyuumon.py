from bs4 import BeautifulSoup
import requests
import pandas as pd

if __name__ == '__main__':
    r = requests.get('https://ja.wikipedia.org/wiki/Python')
    soup = BeautifulSoup(r.content, 'html.parser')
    print(soup.find(class_='mw-redirect').string)
    git_res = requests.get('https://api.github.com/search/repositories?q=language:python+created:2017-07-28&per_page=3')
    # print(pd.DataFrame(git_res.json()['items'])[:][['language', 'stargazers_count', 'git_url', 'updated_at', 'created_at']])
