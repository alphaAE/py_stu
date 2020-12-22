
import matplotlib
import matplotlib.pyplot as plt
import numpy as np


class PlotCanvas:

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

    def scatter(self, axes, number, press):
        axes.scatter(number, press, c='b', marker='o')  # 绘制数据b的散点图

    def bar(self, axes, number, press):
        axes.barh(range(len(number)), number, height=0.3, color='r', alpha=0.8)
        # axes.yticks(range(len(number)), press)  # Y轴出名称显示

    def broken_line(self, axes, number, press):
        axes.plot(number, press, linewidth=1)

    def pie_chart(self, axes, data, label_list):
        axes.pie(data, labels=label_list, autopct="%1.1f%%", pctdistance=0.6)

    def getSubplots(self):
        return plt.subplots(2, 2)

    def show(self, Title='Title', xlabel='', ylabel=''):
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
fig, axes = p.getSubplots()

p.scatter(axes[0, 0], _id, data)
# p.show("散点图（分数分布区间）")

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
p.bar(axes[0, 1], list(intervalDict.values()), list(intervalDict.keys()))
# p.show('柱状图（成绩集中范围）')

# 折线图（增长趋势）
p.broken_line(axes[1, 0], _id, dataSort)
# p.show("折线图（增长趋势）")

# 饼状图（分布概率）
p.pie_chart(axes[1, 1], list(intervalDict.values()), list(intervalDict.keys()))
# p.show("饼状图（分布概率）")

p.show()
