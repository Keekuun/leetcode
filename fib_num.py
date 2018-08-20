#!usr/bin/env/python35
# -*- coding:utf-8 -*-
# author: Keekuun


# 方法一,生成器
def fib1(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield(b)
        a, b = b, a+b
        n = n+1

# 方法二，用递归算法
def fib(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    else:
        return fib(n-2)+fib(n-1)


def fib_num_list(n):
    fib_list = []
    for i in range(1, n+1):
        fib_list.append(fib(i))
    return fib_list


if __name__ == '__main__':
    print(fib(10))
    print(fib_num_list(10))
    # f = fib1(10)
    # for i in range(10):
    #     print(next(f))


# s = (x * x for x in range(5))
# print(s)
# for x in s:
#     print(x)
#
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'
#
#
# f = fib(10)    # generator function
# print('fib(10):', f)
# for x in f:    # 生成器，可以遍历
#     # 第一种方法，用for循环遍历
#     print(x)
#
# # call generator manually:
# g = fib(5)
# while 1:
#     try:
#         x = next(g)
#         # 第二种方法，用next遍历
#         print('g:', x)
#     except StopIteration as e: # 抛出StopIteration错误表示无法继续返回下一个
#         print('Generator return value:', e.value)
#         break
#

