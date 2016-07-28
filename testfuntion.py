#!/usr/bin/env python2
# coding=utf-8
__author__ = 'Hanzhiyun'


# returns the factorial of the argument "number"
def factorial(number):
    if number <= 1:    # base case
        return 1
    else:
        return number * factorial(number - 1)

# def factorial(number):
#     product = 1
#     for i in range(number):
#         product *= (i + 1)
#     return product

user_input = input("Enter a non-negative integer to take the factorial of: ")
factorial_of_user_input = factorial(user_input)
print factorial_of_user_input
