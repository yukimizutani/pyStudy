import matplotlib.pyplot as plt

in1 = '/home/yuki/hdd1/investigation/tcp_bench/rec1_eps.txt'
in2 = '/home/yuki/hdd1/investigation/tcp_bench/rec2_eps.txt'
in3 = '/home/yuki/hdd1/investigation/tcp_bench/rec3_eps.txt'
output = '/home/yuki/hdd1/investigation/tcp_bench/rec_eps.csv'

if __name__ == '__main__':
    f1 = open(in1)
    f2 = open(in2)
    f3 = open(in3)
    rec1s = f1.readlines()
    rec2s = f2.readlines()
    rec3s = f3.readlines()

    out = open(output, 'w')
    eps = []
    eps2 = []
    eps3 = []
    for i in range(len(rec1s)):
        try:
            eps.append(float(rec1s[i]))
            eps2.append(float(rec2s[i]))
            eps3.append(float(rec3s[i]))
            out.write(rec1s[i].rstrip() + ',' + rec2s[i].rstrip() + ',' + rec3s[i])
            out.flush()
        except IndexError:
            print('hey')

    f1.close()
    f2.close()
    f3.close()
    out.close()

    start = 0
    end = 1000
    plt.plot(eps[start:end])
    plt.plot(eps2[start:end])
    plt.plot(eps3[start:end])
    plt.show()
