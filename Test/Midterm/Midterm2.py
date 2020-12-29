# 2 水仙花数
tmpSum = 0
for i in range(1, 1001):
    for j in range(len(str(i))):
        tmpSum += int(str(i)[j])**3
    if tmpSum == i:
        print(i)
    tmpSum = 0
