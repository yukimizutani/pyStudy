import string
import random


def random_string(length):
    val = ''
    for i in range(length):
        val += random.choice(string.ascii_letters)
    return val


def double_quotes(quote_len, val):
    for i in range(quote_len):
        val = '"' + val + '"'
    return val


if __name__ == '__main__':
    f = open('/home/yuki/x-siem/csvde.csv', 'r')

    for l in f.readlines():
        if 'masazane.morimo' in l:
            print(l)
    # f.write('#Comment \r comment\r\n')
    # f.write('head' + '\r\n')

    # f.write(double_quotes(32770, '') + '\r\n')
    # f.write(random_string(32768) + '\r')
    # f.write(random_string(32770) + '\r')
    # f.write(random_string(32765) + '\r\n')

    f.close()
