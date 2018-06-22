# # -*- coding: utf-8 -*-
from numpy import mean

if __name__ == '__main__':
    val = [10, 19, 20]
    print(val[0])
    print(val[-1])

    val = [
        [1, 3, 5, 7, 9],
        [2, 4, 6, 8, 10]
    ]
    print(val[0][3])

    val1 = [1, 2, 3, 4, 5]
    val2 = [6, 7, 8, 9, 10]
    new_val = val1 + val2
    print(new_val)

    val = [1, 2, 3, 4, 5]
    del val[4]  # 要素2を削除
    print(val)

    print(sum(val))
    print(max(val))
    print(mean(val))

    foo = [0, 1, 2, 3, 4] * 8
    foo.append(55)
    foo.extend([66, 67, 68])
    print(len(foo))