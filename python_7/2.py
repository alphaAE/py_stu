# 统计列表重复元素
dataList = ['a', 'a', '2', '3', '2', '4']
resultDict = {}

for item in dataList:
    resultDict[item] = resultDict.get(item, 0) + 1

for item in resultDict.items():
    print("字符 {} 有 {} 个".format(item[0], item[1]))
