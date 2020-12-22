import numpy

# 利用for循环构建一个 y 在 -1.1 到 1.4，x 在 -1.5 到 1.5 的平面
# 并且以固定精度扫描每一个点
for y in numpy.arange(1.4, -1.1, -0.1):
    for x in numpy.arange(-1.5, 1.5, 0.045):
        # 笛卡尔心形函数 即 (x^2 + y^2 -1) - x^2 * y^3 = 0
        f = pow(pow(x, 2) + pow(y, 2) - 1, 3) - pow(x, 2) * pow(y, 3)
        if (f <= 0.0):
            # 小于等于0，即为在函数内的点
            print("*", end='')
        else:
            print(" ", end='')
    print("")
