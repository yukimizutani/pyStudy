import datetime
import urllib

import time
from bs4 import BeautifulSoup
import re
from url.slacking import notify

pattern = r"\((\d+)人／定員(\d+)人\)"
pattern2 = r"人\)(.+)興味あり"
attendants = []


def poke():
    url = "http://twipla.jp/events/212098"
    try:
        res = urllib.request.urlopen(url)
    except urllib.error.URLError as e:
        print(e.reason)
        pass
    else:
        html = res.read()
        soup = BeautifulSoup(html, 'lxml')
        text = soup.get_text().split('\n')
        for li in text:
            if '参加者' in li:
                matcher = re.search(pattern, li)
                if matcher:
                    if matcher.group(1) != matcher.group(2):
                        notify('Somebody cancelled!', True)
                    else:
                        notify('It is full :disappointed:')
                    matcher2 = re.search(pattern2, li)
                    if matcher2:
                        global attendants
                        if len(attendants) != 0:
                            before = attendants
                            after = matcher2.group(1).split('\xa0')[1:]
                            if before != after:
                                notify("They are planning to join: \n" + '\n'.join(matcher2.group(1).split('\xa0')[1:]))
                                diff = list(set(before) - set(after))
                                notify("He/She cancelled! Thanks to " + '\n'.join(diff))
                            else:
                                attendants = matcher2.group(1).split('\xa0')[1:]


if __name__ == '__main__':
    i = 0
    while True:
        poke()
        i += 1
        print('Poked ' + str(i) + ' times at ' + str(datetime.datetime.now()))
        time.sleep(6000)
