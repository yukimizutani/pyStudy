import calendar
from datetime import datetime


def read():
    # mine = 'C:\\Users\\ymizu\\PycharmProjects\\pyStudy\\text\\2020-05_水谷祐貴.csv'
    others = 'C:\\Users\\ymizu\\Downloads\\Att_2020-05_3093_石原摩可.csv'
    input = others

    # , encoding='utf-8'
    f = open(input)
    lines = f.readlines()
    total = 0
    for i, l in enumerate(lines):
        dt = l.rstrip().split(',')[6].split()
        if len(dt) > 1:
            if 0 == i % 2:
                try:
                    end = datetime.strptime(dt[1], '%H:%M')
                except:
                    end = datetime.strptime('23:59', '%H:%M')
                print(end - start)
                total += int((end - start).seconds)
                print(total / 60 / 60)
            else:
                start = datetime.strptime(dt[1], '%H:%M')
    print(total / 60 / 60 - 9 * 18 - 9)


def create():
    pre_id = '444'
    company_id = '3122'

    out = '2020-05_水谷祐貴.csv'
    f = open(out, 'w')
    f.write('データ区分,コード,所属コード1,所属コード2,所属コード3,出退勤区分,打刻時刻,連番')
    num_days = calendar.monthrange(2020, 5)[1]
    for d in range(1, num_days + 1):
        datee = '2020/5/' + str(d)
        f.write(pre_id + ',' + company_id + ',' + ',,,100,' + datee + ',1' + '\n')
        f.write(pre_id + ',' + company_id + ',' + ',,,101,' + datee + ',1' + '\n')
    f.close()


if __name__ == '__main__':
    # create()
    read()
