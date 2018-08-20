import functools
import time


def log2(text=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if isinstance(text, (int, str)):
                print('%s begin call %s():' % (text, func.__name__))
                func(*args, **kw)
                print('%s end call %s():' % (text, func.__name__))
            else:
                print('begin call %s():' % func.__name__)
                func(*args, **kw)
                print('end call %s():' % func.__name__)
            return
        return wrapper
    return decorator if isinstance(text, (int, str)) else decorator(text)


@log2
def now2():
    print('now is:'+time.asctime())


now2()


@log2('timeshow')
def now3():
    print('now is:'+time.asctime())


now3()