#!/usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Hanzhiyun'
import functools


def log(*arg):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            if not arg:
                print('Begin call %s():' % func.__name__)
                func(*args, **kw)
                print('End call %s()!' % func.__name__)
            else:
                print('%s %s():' % (arg[0], func.__name__))
                return func(*args, **kw)
        return wrapper

    return decorator


@log()
def hello():
    print('Hello,World!')

hello()
