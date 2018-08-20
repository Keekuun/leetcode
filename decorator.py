#!usr/bin/env/python35
# -*- coding:utf-8 -*-
# author: Keekuun


import functools


def star(func):
    @functools.wraps(func)
    def wrappers(*args, **kwargs):
        print('*'*50)
        func(*args, **kwargs)
        print('*'*50)
    return wrappers


def percent(func):
    @functools.wraps(func)
    def wrappers(*args, **kwargs):
        print('%\t'*10)
        func(*args, **kwargs)
        print('%\t'*10)
        return func
    return wrappers

@star
@percent
def hello():
    print('\t\t\t\thello')


hello()


def log(msg=''):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if isinstance(msg, (int, str)):
                print(msg)
            else:
                pass
            func(*args, **kwargs)
        return wrapper
    return decorator if isinstance(msg, (int, str)) else decorator(msg)


@log(11)    # int
def hello_world1():
    print('Hello world')


@log('hi_11')    # str
def hello_world2():
    print('Hello world')


@log()    # ()
def hello_world3():
    print('Hello world')


@log    #
def hello_world4():
    print('Hello world')


hello_world1()
hello_world2()
hello_world3()
hello_world4()