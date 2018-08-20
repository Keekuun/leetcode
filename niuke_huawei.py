#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2018/8/1
@user: Keekuun
功能描述
"""

# word = input('>')
# l = len(word.split(' ')[-1])
# print(word)
# print(l)

# a=input().lower()
# b=input().lower()
# print(a.count(b))


# import sys
# while True:
#     try:
#         # sys.stdin.readline()获取从键盘的输入，直至按Enter，.strip()去掉换行符
#         n=int(sys.stdin.readline().strip())
#         L=[]
#         for i in range(n):
#             num=int(sys.stdin.readline().strip())
#             L.append(num)
#         a=list(set(L))
#         a.sort()
#         for i in a:
#             print(i)
#     except:
#         break


# import sys
#
# a = sys.stdin.readline().strip()
# b = sys.stdin.readline().strip()
#
#
# def f(s):
#     l = len(s)
#     n = int(l / 8)
#     for i in range(n):
#         x = i * 8
#         y = x + 8
#         print(s[x:y])
#     if s[n * 8::]:
#         print(s[n * 8::] + '0' * (8 - len(s[n * 8::])))
#
#
# f(a)
# f(b)

# import sys
#
# a = sys.stdin.readline().replace('\n', '')
# b = sys.stdin.readline().replace('\n', '')
# c = [a[i:i + 8] for i in range(0, len(a), 8)]
# d = [b[i:i + 8] for i in range(0, len(b), 8)]
# z = c + d
# for i in z:
#     if len(i) < 8:
#         x = i + (8 - len(i)) * '0'
#         print(x)
#     else:
#         print(i)

# while True:
#     try:
#         n = input()
#         s = eval(n)
#         print(str(s))
#     except:
#         break

# while True:
#     try:
#         print(int(input('二进制'), 2))
#         print(int(input('八进制'), 8))
#         print(int(input('十进制'), 10))
#         print(int(input('十六进制'), 16))
#     except:
#         break

# import sys
#
# n = int(sys.stdin.readline().strip())
# i = 2
# res = ''
# while i * i < n:
#     if n % i == 0:
#         res += str(i) + ' '
#         n = n // i
#     else:
#         i += 1
# res += str(n) + ' '
# print(res)


# a = float(input())
# b = int(a)
# c = a - b
# if c >= 0.5:
#     b +=1
# print(b)


# import sys
#
# n = int(sys.stdin.readline())
# a = {}
# for i in range(n):
#     key, value = map(int, (sys.stdin.readline().split()))
#     if key in a:
#         a[key] += value
#     else:
#         a[key] = value
#
# for j in sorted(a.keys()):
#     print(j, a[j])
#
# s=input()
# list=[]
# for i in s[::-1]: # 反转字符串
#     if i not in list: # 巧妙去重
#         list.append(i)
# str=''
# for i in list:
#     str+=i
# print(str)

# s = input()
# n = 0
# # for i in s:
# #     if not i in w:
# #         w.append(i)
# w = list((set(s)))
# print(w)
#
# for j in w:
#     print(j)
#     if ord(j) > 0 and ord(j) < 127:
#         n += 1
# print(n)



# print(input()[::-1])

import sys
# a = sys.stdin.readline().strip().split(' ')
# print(a)
# s = input().split(' ')
# print(s)
# res = ''
# for i in s[::-1]:
#     res += i+' '
# print(res)


l = input().split(' ')
print(' '.join(l[::-1]))

