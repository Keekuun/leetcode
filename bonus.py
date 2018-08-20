#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2018/8/20
@user: Keekuun

功能描述：
    题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
    利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，
    可提成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时
    高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%
    ，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？

    程序分析：请利用数轴来分界，定位。注意定义时需把奖金定义成长整型。
"""


def bonus():
    I = [100000, 200000, 400000, 600000, 1000000]                           # 公司利润表
    rate = [0.1, 0.075, 0.05, 0.03, 0.015, 0.01]                              # 利率表
    bon = [10000, 7500, 10000, 6000, 6000]                                 # 奖金分配表
    total_bon = 0                                                           # 总奖金
    i = int(input('Please enter the profits of the company:\n\t'))          # 公司实际利润
    if i <= I[0]:  # 100000
        b = i * rate[0]
        bon[0] = b
        for n in range(1, 5):
            bon[n] = 0
    elif i <= I[1]:  # 100000,200000
        b = (i-I[0]) * rate[1]
        bon[1] = b
        for n in range(2, 5):
            bon[n] = 0
    elif i <= I[2]:  # 200000,400000
        b = (i - I[1]) * rate[2]
        bon[2] = b
        for n in range(3, 5):
            bon[n] = 0
    elif i <= I[3]:  # 400000,600000
        b = (i - I[2]) * rate[3]
        bon[3] = b
        for n in range(4, 5):
            bon[n] = 0
    elif i <= I[4]:  # 600000,1000000
        b = (i - I[3]) * rate[4]
        bon[4] = b
        for n in range(5, 5):
            bon[n] = 0
    else:  # 1000000
        b = (i - I[4]) * rate[5]
        bon.append(b)
    for j in bon:
        total_bon += j
    return total_bon


if __name__ == '__main__':
    a = bonus()
    print('The bonus you\'ll get:\n\t%d' % a)