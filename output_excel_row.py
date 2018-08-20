#!/usr/bin/env/python35
# -*- coding:utf-8 -*-
# author: Keekuun

# 输入excel的行号，输出对应行对应的数字（从0开始编号）
# 思路：把26机制转为十进制，值*进制的幂


# 返回字母之间的距离
def sub_str(str_a, str_b):
    return ord(str_a) - ord(str_b)


# 先将字符串列表化，再从最后一位开始取值，进行进制计算和累加,编号从0开始，sum-1
def alpha_to_10(strs):
    result = 0
    list_char = list(strs)
    for index, letter in enumerate(list_char[::-1]):
        result += (sub_str(letter, 'a') + 1) * 26 ** index
    return result - 1


# 请用户输入，调用函数进行输出
# letters = input('请输入英文字母字符串：(输入q/Q退出)')
# print(alpha_to_10(letters))
while True:
    letters = input('请输入英文字母字符串(输入q/Q退出):').lower()
    if letters in ('q', 'Q'):
        break
    print('Excel中对应列的序号为：%s'% alpha_to_10(letters))
