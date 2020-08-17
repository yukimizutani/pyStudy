f = open('C:\\Users\\ymizu\\tmp\\creditDate_2020070201.txt', encoding='utf-8')
f2 = open('out0702', 'w')

prefectureEnum = open('prefectureSvCSV', encoding='utf-8')

if __name__ == '__main__':
    sv = {}
    svs = prefectureEnum.readlines()
    dbs = f.readlines()

    # load prefecture sv
    for l in svs:
        elements = l.rstrip().split(',')
        sv[elements[0]] = elements[1]
    # print(sv)

    nullable = []
    irreg = []
    diff = []
    count = 0
    for l in dbs:
        elements = l.rstrip().split()
        # print(elements)
        if '1' in elements:
            # print(elements.index('1'))
            id = elements.index('1')
            if '1' in elements[id + 1:]:
                # print(elements[id:])
                # print(elements)
                id = id + elements[id + 1:].index('1') + 1
                # print(id)
                # print(elements[id])
            home = sv[elements[4]]
            office = ''
            if elements[id + 1].isdigit():
                print(elements)
                print(elements[id + 1])
                office = sv[elements[id + 1]]
            elif elements[id + 1] == 'NULL':
                nullable.append(elements[0])
            else:
                irreg.append(elements[0])

            if home != office:
                diff.append(elements[0])
                for i, e in enumerate(elements[5:id]):
                    home += e
                for i, e in enumerate(elements[id + 2:len(elements) - 1]):
                    office += e
                print(
                    '{},{},{},{},{}'.format(elements[0], elements[1], elements[2], home, office))
                count += 1
                print(diff)
                print(len(diff))
                print(count)
                print(nullable)
                print(irreg)
                print(len(irreg))
                f2.write('{},{},{},{},{}'.format(elements[0], elements[1], elements[2], home, office) + '\n')
    #     # print(len(elements))
    #     # if len(elements) == 6:
    #     #     print('{},{},{} {}'.format(elements[0], elements[2], elements[3], elements[4]))
    #     # f2.write('{},{},{} {}'.format(elements[0], elements[2], elements[3], elements[4]) + '\n')
    #     # elif len(elements) == 7:
    #     #     print('{}{},{},{} {}'.format(elements[0], elements[1], elements[3], elements[4], elements[5]))
    #     # f2.write('{}{},{},{} {}'.format(elements[0], elements[1], elements[3], elements[4], elements[5]) + '\n')
    #     # else:
    #     #     print('{}{},{},'.format(elements[0], elements[1], elements[3]))
    #     # f2.write('{}{},{},'.format(elements[0], elements[1], elements[3]) + '\n')
        f2.flush()
    f2.close()
