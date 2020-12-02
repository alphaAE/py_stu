import numpy
import pandas
import random


def randchar(start, end, count):
    tmpList = []
    for i in range(count):
        tmpList.append(chr(random.randint(ord(start), ord(end))))
    return tmpList


data = pandas.Series(numpy.random.randint(10, 20, 20), index=randchar('a', 'z', 20))
data2 = pandas.Series(numpy.random.randint(10, 20, 20), index=randchar('a', 'z', 20))

# 取值 切片 运算 排序
print("----------展示----------")
print(data)
print("----------取值----------")
print(data[0])
print("----------切片----------")
print(data[[0, 2, 4]])
print("----------运算----------")
print(data + data2)
print("----------按照索引排序----------")
print(data.sort_index())
print("----------按照值排序----------")
print(data.sort_values())
