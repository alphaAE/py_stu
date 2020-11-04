# 5 字符统计
tmpCount = {}
tmpStr = "000 Python is one of the most beautiful language,是不是老铁！！！"

# tmpStr = input("输入字符串")

for i in tmpStr:
    if (i >= 'A' and i <= 'Z') or (i >= 'a' and i <= 'z'):
        tmpCount["英文字母"] = tmpCount.get("英文字母", 0) + 1
    elif i == ' ':
        tmpCount["空格"] = tmpCount.get("空格", 0) + 1
    elif i >= '0' and i <= '9':
        tmpCount["数字"] = tmpCount.get("数字", 0) + 1
    else:
        tmpCount["其他字符"] = tmpCount.get("其他字符", 0) + 1

print(tmpCount)
