import matplotlib.pyplot as plt

inputFile = '/home/yuki/hdd1/investigation/tcp_bench/rec3_eps.txt'

if __name__ == '__main__':
    f = open(inputFile)
    lines = f.readlines()
    lis = []
    for line in lines:
        lis.append(float(line.rstrip()))
    f.close()
    plt.plot(lis[:1000])
    plt.xlabel("Sample number")
    plt.ylabel("Signal value")
    plt.show()
