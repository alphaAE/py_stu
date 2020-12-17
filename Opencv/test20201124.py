# -*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("./Opencv/img.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

# 截取并覆盖部分原有图层
face = img[100:300, 150:350]
img[0:200, 0:200] = face

# 加入白色噪波
for i in range(5000):
    x = np.random.randint(0, rows)
    y = np.random.randint(0, cols)
    img[x, y, :] = 255

# 均值滤波
result = cv2.blur(img, (5, 5))
# 高斯滤波
result = cv2.GaussianBlur(img, (21, 21), 0)

cv2.imshow("face", result)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
