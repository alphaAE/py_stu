# -*- coding:utf-8 -*-
import cv2
import numpy as np

img = cv2.imread("./Opencv/img.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape

new = np.ones((rows, cols, 1))
new = (img[:, :, 0] + img[:, :, 1] + img[:, :, 2])
print(img)
print(new)


cv2.imshow("new", new)
# 等待显示
cv2.waitKey(0)
cv2.destroyAllWindows()
