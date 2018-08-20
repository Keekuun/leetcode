#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
created on 2018/8/8
@user: Keekuun

宝贝价值：[6,3,5,4,6]
宝贝重量：[2,2,6,5,4]
背包容量（重量）：10
背包可容纳最大价值：15
"""
from functools import reduce

value_list = [6, 3, 5, 4, 6]
weight_list = [2, 2, 6, 5, 4]
bag_volume = 10

sum_value = 0
cost_list = [round(value_list[i] / weight_list[i], 2) for i in range(len(value_list))]

value_tuple = ((value_list[i], weight_list[i]) for i in range(len(value_list)))
print(value_list)
for i in value_tuple:
    print(i)