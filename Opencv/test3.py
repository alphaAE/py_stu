import cv2
import numpy as np

img = cv2.imread("./Opencv/img.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

# 获取图片属性
print(rows, cols, chn)
print(img.size)
print(img.dtype)

# 提取的ROI图像进行融合
face = img[100:300, 150:350]
img[0:200, 0:200] = face
cv2.imshow("face", img)

# 两张图像进行融合
img2 = cv2.imread("./Opencv/img2.jpg", cv2.IMREAD_UNCHANGED)
img2[0:200, 0:200] = face
cv2.imshow("face", img2[0:800, 0:800])

# 提取图像的不同颜色，提取B颜色通道，G、B通道设置为0，则显示蓝色
img2[0:200, 0:200, 2] = 0
img2[0:200, 0:200, 1] = 0
cv2.imshow("face", img2[0:800, 0:800])

# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
