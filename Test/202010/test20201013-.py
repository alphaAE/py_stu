import math


def math99():
    for i in range(1, 10):
        for j in range(1, 10):
            if i >= j:
                print("{:2} *{:2} ={:2}  ".format(i, j, i * j), end="")
        print()


def printTriangle(line):
    for i in range(line):
        print("{}{}".format(' ' * (line - i), '*' * (i * 2 + 1)))


# printTriangle(21)

#       1
#     3   5
#   7   9   11
line = 15
numList = range(1, math.factorial(line), 2)
numListIter = iter(numList)
for i in range(line + 1):
    print("{}".format('    ' * (line - i)), end="")
    for j in range(i):
        print("{:4}".format(next(numListIter)), end="    ")
    print()

### 努力指数
nowYearEffectiveness = 0.01
oneYearEffectiveness = pow((1.0 + 0.01), 365)
print("若一年都为1%: {}".format(oneYearEffectiveness))


def yearEffComp(df):
    tempEff = 1.0
    for i in range(365):
        if i % 7 in [0, 6]:
            tempEff = tempEff * (1 - 0.01)
        else:
            tempEff = tempEff * (1 + df)
    return tempEff


while (yearEffComp(nowYearEffectiveness) < oneYearEffectiveness):
    nowYearEffectiveness += 0.001
print("每天努力指数: {:.3}".format(nowYearEffectiveness))

### 1 - 1000内的回文
# for i in range(1,1001):
#     if str(i)[::-1] == str(i):
#         print(i, end=" ")
