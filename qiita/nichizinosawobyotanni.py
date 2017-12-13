from _datetime import datetime

# year,month,day,hour,minute,second(,micro?)がdatetimeメソッドの引数
first = "13:37:17.798"
second = "14:42:31.160"
formatt = "%H:%M:%S.%f"
delta = datetime.strptime(second, formatt) - datetime.strptime(first, formatt)
print(100000 / delta.total_seconds())
