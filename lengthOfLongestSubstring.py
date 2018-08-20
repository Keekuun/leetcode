# -*- coding:utf-8 -*-
# author : Keekuun

"""
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
"""


def length_of_longest_substring(s):
    substring = []  # 储存所有的子串
    length = 1
    index = 1
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if len(s[i:j]) == len(set(s[i:j])):  # 筛选出无重复的子串
                substring.append(s[i:j])
    print(substring)
    for i, s in enumerate(substring):
        if len(s) > length:
            length = len(s)
            index = i
    print('最长子串为：{},\t长度为：{}'.format(substring[index], length))
    return length


length_of_longest_substring('pwwkew')

