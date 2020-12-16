
import matplotlib
import matplotlib.pyplot as plt
import numpy


class PlotCanvas:

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

    def bar(self, number, press):
        # 从下往上画水平条形图
        plt.barh(range(len(number)), number, height=0.3, color='r', alpha=0.8)
        plt.yticks(range(len(number)), press)  # Y轴出名称显示

    def broken_line(self, x, y):
        plt.plot(x, y, linewidth=1)  # 绘制折线

    def show(self):
        plt.xlabel('xlabel')
        plt.ylabel('ylabel')
        plt.title('Title')
        plt.grid()  # 显示网格
        plt.show()  # 显示折线图


tmpFile = open("./Test/data.txt", "r", encoding="utf-8")
dataStr = tmpFile.readlines()
data = list()

for s in dataStr:
    data.append(float(s.replace('\n', '').replace(' ', '')))

p = PlotCanvas()
p.bar(list(range(len(data))), data)
p.show()

p = PlotCanvas()
p.broken_line(list(range(len(data))), data)
p.show()
