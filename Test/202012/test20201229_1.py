import csv

dictData = dict()

# 读取csv构造字典
with open("./OutFile/data2.csv", "r", encoding="utf8", newline='') as _file:
    _reader = csv.reader(_file)
    for item in _reader:
        dictData[item[0]] = item[1]

print(dictData)

# 查询部分
while True:
    inStr = input("输入查询字符:")
    result = dictData.get(inStr, None)

    if result is None:
        print("查无此词，向字典追加 [{}]:".format(inStr))
        value = input()
        dictData[inStr] = value
        # 遍历字典保存csv
        with open("./OutFile/data2.csv", "w", encoding="utf8", newline='') as _file:
            _writer = csv.writer(_file)
            for item in dictData.items():
                _writer.writerow(item)
        print("追加完成 [{}: {}]:".format(inStr, value))
        continue
    else:
        print("查询到结果 [{}]".format(result))
