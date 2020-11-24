# 函数 递归

# 斐波那契数列
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


tmpList = []

for i in range(1, 21 + 1):
    tmpList.append(fib(i))

print(tmpList)


# 阶乘
def gc(n):
    if n <= 1:
        return 1
    return gc(n - 1) * n


print(gc(10))


# 反转字符串
def reverse(s):
    if s == "":
        return ""
    return reverse(s[1:]) + s[0]


tmpStr = "123456789"
print(tmpStr[::-1])
print(reverse(tmpStr))
