# 图形画布
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
import matplotlib  # 导入图表模块
import matplotlib.pyplot as plt  # 导入绘图模块
import numpy


class PlotCanvas:

    def __init__(self, parent=None, width=0, height=0, dpi=100):
        # 避免中文乱码
        matplotlib.rcParams['font.sans-serif'] = ['SimHei']
        matplotlib.rcParams['axes.unicode_minus'] = False

    def broken_line(self, x, y):
        '''
        y:y轴折线点，也就是价格
        linewidth:折线的宽度
        color：折线的颜色
        marker：折点的形状
        markerfacecolor：折点实心颜色
        markersize：折点大小
        '''
        plt.plot(x, y, linewidth=1)  # 绘制折线

    def show(self):
        plt.xlabel('xlabel')
        plt.ylabel('ylabel')
        plt.title('Title')
        plt.grid()  # 显示网格
        plt.show()  # 显示折线图


p = PlotCanvas()
x = list()
y = list()

diaoLine = [(4, 2), (3, 1), (2, 1), (1, 2), (1, 3), (2, 4), (3, 4), (4, 3),
            (4, 10), (5, 11), (6, 11), (7, 10),
            (7, 3), (8, 4), (9, 4), (10, 3), (10, 2), (9, 1), (8, 1), (7, 2)]
for tX, tY in diaoLine:
    x.append(tX)
    y.append(tY)

p.broken_line(x, y)

p.show()
