import codecs
import chardet

inputFile = '/home/yuki/xsiem_packages/1.2.3-beta1/Logstorage-xsiem-v1.2.3/master/u8_export_userlist.csv'
output = '/home/yuki/xsiem_packages/1.2.3-beta1/Logstorage-xsiem-v1.2.3/master/export_userlist.csv'


def guess():
    f = open(inputFile, 'rb')
    encoding = chardet.detect(f.read())
    print(encoding)
    f.close()
    return encoding


def read(encoding, should_write):
    f2 = codecs.open(inputFile, 'r', encoding['encoding'])
    f3 = codecs.open(output, 'w', 'shift_jis', 'ignore')
    for i, l in enumerate(f2):
        print(l.rstrip())
        if should_write:
            f3.write(l.rstrip() + '\n')
    f2.close()
    f3.close()


if __name__ == '__main__':
    encd = guess()
    read(encd, True)
