# -*- coding: utf-8 -*-

import requests

SLACK_CHANNEL_ID = 'C011H6YATQE'
SLACK_URL = "https://slack.com/api/channels.history"
TOKEN = "xoxp-786802567300-980832260678-1090416060113-130320578fdeaf91728a49f24fcac870"
after = 'Upsert failed. First exception on row 0; first error:'
dic = {}


def fetch_text():
    payload = {
        "channel": SLACK_CHANNEL_ID,
        "token": TOKEN,
        "count": 100
    }
    response = requests.get(SLACK_URL, params=payload)
    json_data = response.json()
    msgs = json_data['messages']
    for msg in msgs:
        file = msg['files'][0]
        if 'データ連携エラー' in file['title']:
            err = file['plain_text'][100:]
            id = file['plain_text'][20:48]
            if err in dic.keys():
                if id not in dic[err]:
                    dic[err].append(id)
            else:
                dic[err] = [id]
            print(err)
            print(id)


if __name__ == '__main__':
    fetch_text()
    f = open('out', 'w')
    for k in dic.keys():
        print(k)
        f.write(k.replace('r: ', '') + '\n')
        for element in dic[k]:
            print(element.split(':')[1])
            f.write(element.split(':')[1].replace('】U', '') + '\n')

    f.flush()
    f.close()
