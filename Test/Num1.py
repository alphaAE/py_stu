
arr = [171,162,155,184,445,362,351,689,772]

# 均值
sumNumTemp = 0
for i in arr:
    sumNumTemp += i
avgNum = sumNumTemp / len(arr)
print("均值：{:.3f}".format(avgNum))

# 方差
varianceArr = []
for i in arr:
    varianceArr.append((i - avgNum) ** 2)
print(varianceArr)




# 标准差