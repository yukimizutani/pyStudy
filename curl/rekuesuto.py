from bs4 import BeautifulSoup
import requests

payload = {
    'identity': 'ymizutani',
    'password': 'syokotan4'
}

s = requests.Session()
r = s.get('http://source.dev.infoscience.co.jp:8080/jamwiki/en/Special:Login')
soup = BeautifulSoup(r.text)
auth_token = soup.find(attrs={'name': 'authenticity_token'}).get('value')
payload['authenticity_token'] = auth_token

# ログイン
s.post('http://source.dev.infoscience.co.jp:8080/jamwiki/en/Special:Login', data=payload)
