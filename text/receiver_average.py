inputFile = '/home/yuki/hdd1/investigation/tcp_bench/rec3_eps.txt'

if __name__ == '__main__':
    f = open(inputFile)
    previous = None
    lines = f.readlines()
    eps = []
    for line in lines:
        eps.append(float(line.rstrip()))
    print(max(eps))
    print(sum(eps)/len(eps))
    f.close()
