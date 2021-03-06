# 4-6 蒙特卡罗方法求解π值
from random import random
from math import sqrt
import time
DARTS = 1000
hits = 0.0
time.perf_counter()
for i in range(1, DARTS + 1):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits / DARTS)
print("Pi值是{}.".format(pi))
print("运行时间是: {:5.5}s".format(time.perf_counter()))
