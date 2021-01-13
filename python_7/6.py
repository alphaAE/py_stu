import matplotlib
import matplotlib.pyplot as plt
import numpy

x = ['a', 'b', 'c', 'd']
y = [1, 2, 5, 3]

# 柱状图
plt.bar(x, y, color='r', alpha=0.8)

# 折线图
plt.plot(x, y)

# 饼图
plt.pie(y, labels=x)

# 散点图
plt.scatter(y, x)

plt.title("Title")
plt.xlabel("x")
plt.ylabel("y")
plt.grid()  # 显示网格
plt.show()
