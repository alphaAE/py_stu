
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class PlotCanvas:

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

    def scatter(self, number, press):
        plt.scatter(number, press, c='b', marker='o')  # 绘制数据b的散点图

    def bar(self, number, press):
        plt.barh(range(len(number)), number, height=0.3, color='r', alpha=0.8)
        plt.yticks(range(len(number)), press)  # Y轴出名称显示

    def broken_line(self, number, press):
        plt.plot(number, press, linewidth=1)

    def pie_chart(self, data, label_list):
        plt.pie(data, labels=label_list, autopct="%1.1f%%", pctdistance=0.6)

    def show(self, Title='', xlabel='', ylabel=''):
        plt.title(Title)
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.grid()  # 显示网格
        plt.show()  # 显示折线图


# 读取并处理数据
tmpFile = open("./Test/data.txt", "r", encoding="utf-8")
dataStr = tmpFile.readlines()
data = list()
for s in dataStr:
    data.append(float(s.replace('\n', '').replace(' ', '')))
dataSort = data.copy()
dataSort.sort()
_id = list(range(1, len(data) + 1))

# 散点图（分数分布区间）
p = PlotCanvas()
p.scatter(_id, data)
p.show("散点图（分数分布区间）")

# 柱状图（成绩集中范围）
sill = 10
tmpIntervalList = list(range(0, 101, sill))
intervalDict = {}
for i in data:
    for j in tmpIntervalList:
        if i < j:
            t = intervalDict.get((str(j - sill) + "-" + str(j)), 0)
            intervalDict[(str(j - sill) + "-" + str(j))] = t + 1
            break
p = PlotCanvas()
p.bar(list(intervalDict.values()), list(intervalDict.keys()))
p.show('柱状图（成绩集中范围）')

# 折线图（增长趋势）
p = PlotCanvas()
p.broken_line(_id, dataSort)
p.show("折线图（增长趋势）")

# 饼状图（分布概率）
p = PlotCanvas()  # 创建画布对象
p.pie_chart(list(intervalDict.values()), list(intervalDict.keys()))
p.show("饼状图（分布概率）")
