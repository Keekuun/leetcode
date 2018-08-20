#!usr/bin/env/python35
# -*- coding:UTF-8 -*-
# author: Keekuun

import functools
import time


def log(msg1, msg2):
    def decorator(func):
        @functools.wraps(func)
        def wrappers(*args, **kw):
            print(msg1)
            print('开始运行%s()函数' % func.__name__)
            start = time.time()
            print([i for i in func(*args, **kw)])
            print(msg2 + '{:.2f}'.format((time.time()-start)*1000)+ 'ms')
        return wrappers
    return decorator


@log('计算函数运行时间', '运行时间为：')
def fib(max):
    a, b, n = 0, 1, 0
    while n < max:
        yield(b)
        a, b = b, a+b
        n = n+1

fib(200)