# -*- coding:utf-8 -*-
# author : Keekuun

"""
有三根杆子A，B，C。A杆上有N个(N>1)穿孔圆盘，盘的尺寸由下到上依次变小。要求按下列规则将所有圆盘移至C杆：

每次只能移动一个圆盘；

大盘不能叠在小盘上面。

"""

time = 0


def mov(n, a, b, c):
    global time
    # 当只有一个圆盘时
    if n == 1:
        print(a, '-->', c)
        time += 1
    # 当有n个圆盘时
    else:
        # n = (n-1)+1,先移动n-1个圆盘到B
        mov(n - 1, a, c, b)
        # 把最大的圆盘1直接移到C
        mov(1, a, b, c)
        # 再把n-1个圆盘从B移到C
        mov(n - 1, b, a, c)
        time -= 1
    return time


print(mov(1, 'A', 'B', 'C'))
print('*' * 10)
print(mov(2, 'A', 'B', 'C'))
print('*' * 10)
print(mov(3, 'A', 'B', 'C'))
print('*' * 10)
print(mov(4, 'A', 'B', 'C'))
