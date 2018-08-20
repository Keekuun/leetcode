#!/usr/bin/python
# -*- coding: UTF-8 -*-
# author:FunC_ZKK
"""
    题目：一个标准的科学实验是，抛球并且看它能够弹跳多高。一旦球的“弹跳性”已经确定了，
这个比率值就会给出弹跳性的指数。例如，如果球从10米高落下弹跳到6米高，这个索引就是
0.6，并且球在一次弹跳之后总的运动距离是16米。如果球继续弹跳，两次弹跳后的距离将会
是10米+6米+6米+3.6米=25.6米。注意，每次后续的弹跳运动的距离，都是到地板的距离加上
这个距离的0.6倍，这个0.6倍就是球反弹回来的距离。编一个程序，让用户输入球的一个初始
高度以及允许球持续弹跳的次数。输出球的运动的总距离。
"""
#import pdb

#pdb.set_trace()
def bounce_height_recursion(h, n, rate=0.6):
    '''递归实现'''
    sum = h+0.6*h
    if n == 1:
        return sum
    else:
        sum += sum * 0.6
        return sum


if __name__ == '__main__':
    h = int(input('Please enter the height of the ball:\n'))
    n = int(input('Please enter the bounce times of the ball:\n'))
    print(bounce_height_recursion(h, n))