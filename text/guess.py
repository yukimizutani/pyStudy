import codecs
import chardet

inputFile = '/home/yuki/Downloads/土屋様依頼事項.txt'
output = '土屋.txt'


def guess():
    f = open(inputFile, 'rb')
    encoding = chardet.detect(f.read())
    print(encoding)
    f.close()
    return encoding


def read(encoding, should_write):
    f2 = codecs.open(inputFile, 'r', encoding['encoding'])
    f3 = open(output, 'w')
    for i, l in enumerate(f2):
        print(l.rstrip())
        if should_write:
            f3.write(l.rstrip() + '\n')
    f2.close()
    f3.close()


if __name__ == '__main__':
    encd = guess()
    read(encd, True)
