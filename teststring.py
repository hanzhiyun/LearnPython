#!/usr/bin/env python2
# coding=utf-8
__author__ = 'Hanzhiyun'

a = "My first test string"
b = 'Another test string that I have defined'
c = "This is Sal's string"
d = 'My favorite word is "asparagus", what is yours?'
math_string = "3+4*2"
expression_string = "a+' '+b+' tiger'"


print a
print b
print c
print d
print math_string
print expression_string
print len(a)
print len(math_string)

a_with_b = a + b
print a_with_b
b_with_a = b + a
print b_with_a

print math_string + expression_string

print b.split(' ')
print b.split('t')
print math_string.find('*')
print math_string.find('3')
print c.replace('i', 'o')
print c
c = c.replace('i', 'o')
print c

print eval(math_string)
print eval(math_string + '1')
print eval(expression_string)

#raw_input()
import os
os.system('pause')
