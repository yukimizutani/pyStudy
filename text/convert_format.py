import json
import csv
import sys

input = '/home/yuki/x-siem/utils/commands-main/src/test/resources/kasperskyData.json'
output = '_kaspersky.csv'

if __name__ == '__main__':
    f = open(input)
    data_parsed = json.loads(f.read())

    header = []
    limit = 7
    # for key in data_parsed[0].keys():
    #     for i in xrange(int(len(data_parsed[0].keys())/2)):
    #         header.append(key)
    for index, key in zip(range(limit), data_parsed[0].keys()):
        header.append(key)
    f = csv.writer(open(str(limit) + output, "w"))
    f.writerow(header)
    max_lines = 10

    stats = {}
    for i in range(0, max_lines):
        meetup = list(data_parsed[i].values())
        meetuped = []
        for m in range(limit):
            meetuped.append(meetup[m])
            if m not in stats.keys():
                stats[m] = sys.getsizeof(meetup[m])
            else:
                stats[m] += sys.getsizeof(meetup[m])
        f.writerow(meetuped)
