# 杨辉三角
line = 12
dList = [1]

for i in range(line):
    print('   ' * (line - 1 - i), end='')
    for j in dList:
        print("{:6}".format(j), end='')
    print()

    tmpList = [1]
    for j in range(len(dList) - 1):
        tmpList.append(dList[j] + dList[j + 1])
    tmpList.append(1)
    dList = tmpList
