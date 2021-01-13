# 回文
strIn = "asdfdsa"

if strIn == strIn[::-1]:
    print("{} 是回文".format(strIn))
else:
    print("{} 不是回文".format(strIn))

# 完数 1 - 1000
for n in range(1, 1001):
    tmpList = []
    for i in range(1, n):
        if n % i == 0:
            tmpList.append(i)
    if sum(tmpList) == n:
        tmpList = map(str, tmpList)
        print("{} = {}".format(n, '+'.join(tmpList)))

# 水仙花数
for n in range(100, 1001):
    sum = 0
    for i in str(n):
        sum += int(i)**3
    if n == sum:
        print(n)
