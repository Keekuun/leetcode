#!/usr/bin/env/python35
# -*- coding:utf-8 -*-
# author: Keekuun

# 16进制就是逢16进1


def distance(num1, num2):
    # 求与第一个数（0）的距离
    if ord(num1) >= 65:
        # 输入的是A,B,C,D,E
        return ord(num1) - ord(num2) - 7
    else:
        # 输入的是0-9
        return ord(num1) - ord(num2)


def sixteen_to_ten(num):
    result = 0
    for index, value in enumerate(num[::-1]):
        # 分别将各个位数转化为10进制，然后求和
        result += distance(value, str('0')) * 16 ** index
        # print('result=%s'%result)
    return result


num = list(input('请输入16进制数(不添加0x)：').upper())
print(sixteen_to_ten(num))






