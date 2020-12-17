import cv2
import numpy as np

img = cv2.imread("./Opencv/img.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

# 使用Numpy的itemset函数修改像素后读取
img.itemset((78, 100, 0), 100)
img.itemset((78, 100, 1), 110)
img.itemset((78, 100, 2), 120)
blue = img.item(78, 100, 0)
green = img.item(78, 100, 1)
red = img.item(78, 100, 2)
print(blue)
print(green)
print(red)
