f = open('dealer', encoding='utf-8')
f2 = open('dealer2', encoding='utf-8')

if __name__ == '__main__':
    lines = f.readlines()
    lines2 = f2.readlines()
    diff = []
    for i, l in enumerate(lines):
        if l not in lines2:
            diff.append(l.rstrip())
    print(diff)
    print(len(diff))
        # print(elements)
        # if len(elements) == 11:
        # print(elements[1])
        # print(elements[5], elements[6])
        # else:
        # print(elements[1])
        # print(elements[6], elements[7])
