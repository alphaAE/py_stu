# 4 完数
factorList = []

for i in range(1, 1001):
    # 取所有因子
    for j in range(1, i):
        if i % j == 0:
            factorList.append(j)

    if i == sum(factorList):
        for j in range(len(factorList)):
            if j == 0:
                tmpStr = "{}={}".format(i, str(factorList[0]))
            else:
                tmpStr += "+{}".format(factorList[j])

        print(tmpStr)
    factorList.clear()
