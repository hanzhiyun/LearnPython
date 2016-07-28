# coding=utf-8
__author__ = 'Hanzhiyun'


def fibonacci(n):
    print("fibonacci: "+str(n))
    if n == 0 or n == 1:  # if n < 2:
        return n
    else:
        return (fibonacci(n - 1) + fibonacci(n - 2))
