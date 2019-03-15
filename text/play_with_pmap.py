if __name__ == '__main__':
    f = open('/home/yuki/tmp/pmap/pmap')
    sum_virt = 0
    sum_res = 0
    pmap = {}
    pmap['anon'] = 0
    for l in f.readlines():
        # print(l.split())
        # print(len(l.split()))
        columns = l.split()
        if len(columns) == 6 and columns[3].isdigit():
            if columns[5] not in pmap.keys():
                pmap[columns[5]] = int(columns[3])
            else:
                pmap[columns[5]] += int(columns[3])
        if len(columns) == 8:
            pmap['anon'] += int(columns[3])
        if len(columns) == 6 or len(columns) == 8:
            virt = columns[1]
            if virt.isdigit():
                sum_virt += int(virt)
                sum_res += int(columns[3])
                print(sum_virt / 1024 / 1024)
                print(sum_res)
    for k, v in sorted(pmap.items(), key=lambda x: x[1]):
        print(str(k) + ": " + str(v))
        # if len(columns) == 6 and 'libjli.so' in columns[5]:
        #     virt = columns[1]
        #     if virt.isdigit():
        #         sum_virt += int(virt)
        #         sum_res += int(columns[3])
        #         print(sum_virt / 1024 / 1024)
        #         print(sum_res)