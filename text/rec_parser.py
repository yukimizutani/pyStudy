inputFile = '/home/yuki/nemesis/rec2.log'
output = '/home/yuki/hdd1/investigation/tcp_bench/rec2_eps.txt'

if __name__ == '__main__':
    f = open(inputFile)
    f2 = open(output, 'w')
    previous = 0
    total_diff = 0
    lines = f.readlines()
    for line in lines:
        if previous is not 0:
            diff = int(line.rstrip().split()[5]) - previous
            print(diff)
            total_diff += diff
            if diff > 3:
                f2.write(str(1000 / diff * 1000 / 3) + '\n')
            else:
                f2.write(str(0) + '\n')
            f2.flush()
            previous = int(line.rstrip().split()[5])
        else:
            previous = int(line.rstrip().split()[5])
    f.close()
    print(len(lines))
    f2.close()
