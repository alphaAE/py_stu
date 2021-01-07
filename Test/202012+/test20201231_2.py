# 字符串切片取值
def isNarcissus(num):
    n = 0
    for i in str(num):
        n += int(i) ** 3
    return num == n


# 数值计算取值
def isNarcissus2(num):
    tmpNum = num
    n = 0
    while tmpNum > 0:
        n += (tmpNum % 10) ** 3
        tmpNum = tmpNum // 10
    return num == n


for n in range(100, 1000):
    if isNarcissus(n):
        print("1:" + str(n))
    if isNarcissus2(n):
        print("2:" + str(n))
