# coding=utf-8
__author__ = 'Hanzhiyun'

# calculate the factorial
number = input("Enter a non-negative integer to take the factorial of: ")

product = 1
for i in range(number):
    product *= (i + 1)

print(product)
