# coding utf-8
import time
import requests
from requests.auth import HTTPBasicAuth
from _datetime import datetime as dt, timedelta

f = open('record.csv', 'a')
current_size = 0
previous_size = 0


def main():
    # GETパラメータはparams引数に辞書で指定する

    response = requests.get(
        'http://xsiem01:8090/v1/command/admin/taskmanager',
        auth=HTTPBasicAuth('admin', 'admin'))
    # レスポンスオブジェクトのjsonメソッドを使うと、
    # JSONデータをPythonの辞書オブジェクトを変換して取得できる
    obj = response.json()
    current = dt.now()

    received_date = dt.strptime(obj['resources'][0]['resource']['receivedTime'], '%Y-%m-%dT%H:%M:%S.%fZ') + timedelta(
        hours=9)
    print('Received: {}'.format(received_date))
    print('Current: {}'.format(current))

    current_size = obj['resources'][0]['resource']['progress'][1]['outputSize']
    print('Output: {}'.format(current_size))

    print('EPS: {0:.2f}'.format(int(current_size) / (current - received_date).seconds))
    # print(received_date.timestamp() * 1000)
    f.write('{},{},{},{}\n'.format(current, received_date, current_size,
                                   int(current_size) / (current - received_date).seconds))
    f.flush()


if __name__ == '__main__':
    f.write('Current,Received,Output,EPS\n')
    for i in range(0, 10000):
        main()
        time.sleep(30)
    f.close()
