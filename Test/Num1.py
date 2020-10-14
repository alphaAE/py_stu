import math

arr = [171,162,155,184,445,362,351,689,772]

# 均值
avgNum = sum(arr) / len(arr)
print("均值：{:.3f}".format(avgNum))

# 方差
varianceArr = []
for i in arr:
    varianceArr.append((i - avgNum) ** 2)
variance = sum(varianceArr) / len(varianceArr)
print("方差：{:.3f}".format(variance))

# 标准差
standardDeviation = math.sqrt(variance)
print("标准差：{:.3f}".format(standardDeviation))
