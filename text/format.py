if __name__ == '__main__':
    # ver = 'beta2'
    # tes = 'Test '
    # reviewer = 'Yuki'
    # result = 'Good'
    # comments = ''
    # print('|_. Version |_. Test  |_. Reviewer |_. Result |_. Comments |')
    # for i in range(1, 17):
    #     print('|{}|{}|{}|{}|{}|'.format(ver, tes + str(i), reviewer, result, comments))
    f = open('tes', 'r')
    for l in f.readlines():
        ls = l.replace('\n', '').split(' ')
        print(ls[len(ls) - 1])
