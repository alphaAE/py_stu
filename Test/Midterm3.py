# 3 兔子增速
# 斐波那契数列
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


tmpList = []

for i in range(1, 21 + 1):
    tmpList.append(fib(i))

print(tmpList)
