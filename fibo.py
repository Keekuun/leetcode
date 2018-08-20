# -*- coding:utf-8 -*-
# author : Keekuun

"""
斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契（Leonardoda Fibonacci）以兔子繁殖为例子而引入，
故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34...
"""


def fibo1(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        # print(b)
        a, b = b, a + b
        n += 1


for i in fibo1(9):
    print(i)
print(fibo1(9))
print('*' * 10)


def fibo2(n):
    if n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        return fibo2(n - 1) + [fibo2(n - 1)[-1] + fibo2(n - 1)[-2]]

print(fibo2(9))