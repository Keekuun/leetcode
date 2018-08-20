# -*- coding:utf-8 -*-
# author : Keekuun

"""
杨辉三角形，又称贾宪三角形，帕斯卡三角形，是二项式系数在三角形中的一种几何排列。规律如下：
         1                         0 1
        1 1                \     + 1 0     0 1 1
       1 2 1        --------\   --------  +1 0 0    0 1 2 1     0 1 3 3 1
      1 3 3 1       --------/      1 1   --------  +1 2 1 0    +1 3 3 1 0
     1 4 6 4 1             /               1 2 1   ---------   ----------
    ''''''''''                                      1 3 3 1     1 4 6 4 1
"""

# 补充知识zip函数：

a = [1, 2, 3]
b = [4, 5, 6]
c = [4, 5, 6, 7]
ab_zip = zip(a, b,c)
ab_list = list(ab_zip)
ac_zip = zip(a, c)
ac_list = list(ac_zip)
ac = list(zip(*ab_zip))

print(ab_zip)
print(ac_zip)
print(ab_list)
print(ac_list)
print(*ab_list)

print('*' * 50)
print('*' * 50)


def triangle1(n):
    if n == 1:
        return [1]
    else:
        return [sum(i) for i in zip((triangle1(n - 1) + [0]), [0] + triangle1(n - 1))]


for i in range(1, 11):
    print(triangle1(i))

print('*' * 50)
print('*' * 50)


def triangle2():
    L = [1]
    while True:
        yield L
        L = [sum(i) for i in zip((L + [0]), [0] + L)]


n = 0
for i in triangle2():
    print(i)
    n += 1
    if n >= 10:
        break


