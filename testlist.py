# coding=utf-8
__author__ = 'Hanzhiyun'

a = [1, -1, 0, 0, 5, 10]
a[4] = "this text"
print a
a[0] = [-1, -2]
print a

# Data space is the same
b = [7, 13, 15]
c = b
# c and b pointing the same space
print (b, c)
c[0] = 1
print (b, c, "b and c are the same ")

# copy b to d
d = b[:]
print (b, d)
d[0] = 7
print (b, d, "b and d are different")

# e is including in b
e = b[0:2]
print(b, e)

# add new element to the end of b
b.append("new element")
print b
