from datetime import datetime

inputFile = '/home/yuki/hdd1/investigation/tcp_bench/test2/gid.txt'
output = '/home/yuki/hdd1/investigation/tcp_bench/test2/receiver_eps.txt'

if __name__ == '__main__':
    f = open(inputFile)
    f2 = open(output, 'w')
    previous = None
    for line in f.readlines():
        if previous is not None:
            delta = datetime.strptime(line.rstrip().split()[1], "%H:%M:%S.%f") - previous
            diff = delta.total_seconds()*1000
            if diff is not 0:
                f2.write(str(0) + '\n')
            else:
                f2.write(str(10000 / diff * 1000) + '\n')
            f2.flush()
            previous = datetime.strptime(line.rstrip().split()[1], "%H:%M:%S.%f")
        else:
            previous = datetime.strptime(line.rstrip().split()[1], "%H:%M:%S.%f")
    f.close()
    f2.close()
