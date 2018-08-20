# -*- coding:utf-8 -*-
# author : Keekuun

# 列表生成式,list
l1 = [i for i in range(10)]
# 或者
l2 = list(range(10))
print(l1, l2)
# type(l) list
# 打印：[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

l3 = [x * x for x in range(1, 11) if x % 2 == 0]
print(l3)

l4 = [m + n for m in 'ABC' for n in 'XYZ']
print(l4)

# 生成器,generator:惰性，可迭代
g = (i for i in range(10))
print(g)
# 打印：<generator object <genexpr> at 0x0000027EC76F5F10>
for i in g:
    print(i)
