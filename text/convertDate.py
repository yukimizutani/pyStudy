import datetime as dt

f = open('C:\\Users\\ymizu\\OneDrive\\デスクトップ\\dataloader_win\\contract.csv')
f2 = open('contract_dates', 'w')

if __name__ == '__main__':
    for l in f.readlines():
        elements = l.rstrip().split(',')
        try:
            jst_now = dt.datetime.fromisoformat(elements[1].replace('Z', '')) + dt.timedelta(hours=9)
            f2.write(
                jst_now.strftime('%Y-%m-%d %H:%M:%S') + '\n')
        except:
            continue
        f2.flush()
    f2.close()
