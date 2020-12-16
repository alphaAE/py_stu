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

    def broken_line(self, y):
        '''
        y:y轴折线点，也就是价格
        linewidth:折线的宽度
        color：折线的颜色
        marker：折点的形状
        markerfacecolor：折点实心颜色
        markersize：折点大小
        '''
        x = list(range(1, 101))
        plt.plot(x, y, linewidth=1)  # 绘制折线

    def show(self):
        plt.xlabel('xlabel')
        plt.ylabel('ylabel')
        plt.title('Title')
        plt.grid()  # 显示网格
        plt.show()  # 显示折线图


p = PlotCanvas()

for i in range(100):
    y1 = numpy.random.randint(10, 100, 100)
    p.broken_line(y1)

p.show()
