import csv
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

headers = ['class', 'name', 'sex', 'height', 'year']

rows = [
    [1, 'xiaoming', 'male', 168, 23],
    [1, 'xiaohong', 'female', 162, 22],
    [2, 'xiaozhang', 'female', 163, 21],
    [2, 'xiaoli', 'male', 158, 212]
]

# WRITE
# with open("./OutFile/test.csv", "w", encoding="UTF8", newline='') as f:
#     csvF = csv.writer(f)
#     csvF.writerow(headers)
#     csvF.writerows(rows)

with open("./OutFile/test.csv", "w", encoding="UTF8", newline='') as f:
    for row in rows:
        _str = ",".join(map(str, row))
        f.write(_str + "\n")

print("Success.")


# READ
# with open("./OutFile/test.csv", "r", encoding="UTF8", newline='') as f:
#     _reader = csv.reader(f)
#     for row in _reader:
#         print(row)

with open("./OutFile/test.csv", "r", encoding="UTF8", newline='') as f:
    tmpData = list()
    for row in f.readlines():
        tmpData.append(row.replace("\n", "").split(","))
    # 制表
    matplotlib.rcParams['font.sans-serif'] = ['SimHei']
    matplotlib.rcParams['axes.unicode_minus'] = False
    plt.barh([i[1] for i in tmpData],
             [int(i[3]) + 10 for i in tmpData],
             height=0.3, color='g', alpha=0.6)
    plt.barh([i[1] for i in tmpData],
             [int(i[3]) for i in tmpData],
             height=0.3, color='r', alpha=0.6)
    plt.barh([i[1] for i in tmpData],
             [int(i[3]) - 10 for i in tmpData],
             height=0.3, color='b', alpha=0.6)
    plt.xlim(140, 180)
    # plt
    plt.grid()
    plt.show()
