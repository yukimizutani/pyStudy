import codecs
import chardet

inputFile = 'C:\\Users\\ymizu\\Downloads\\Att.2020-04_30_楠木椋.csv'
output = './out2'


def guess():
    f = open(inputFile, 'rb')
    encoding = chardet.detect(f.read())
    print(encoding)
    f.close()
    return encoding


def read(encoding, should_write):
    f2 = codecs.open(inputFile, 'r', encoding['encoding'])
    f3 = codecs.open(output, 'w', 'utf-8')
    for i, l in enumerate(f2):
        print(l.rstrip())
        if should_write:
            f3.write(l.rstrip() + '\n')
    f2.close()
    f3.close()


if __name__ == '__main__':
    encd = guess()
    # read(encd, True)
