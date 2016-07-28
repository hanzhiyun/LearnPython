# coding=utf-8
__author__ = 'Hanzhiyun'

a = [7, 3, 1, 2, 4, 6, 4, 6, 7, 10, 32, 3, 2]


def insertion_sort(list):
    for index in range(1, len(list)):
        value = list[index]
        i = index - 1
        while i >= 0 and (value < list[i]):
            list[i + 1] = list[i]  # shift number in slot i right to slot i+1
            list[i] = value  # shift value left into solt i
            i -= 1


insertion_sort(a)
print a
