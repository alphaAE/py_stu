import cv2
import numpy as np

# 读入一张图片并显示保存
img = cv2.imread("./Opencv/img.jpg", cv2.IMREAD_UNCHANGED)
rows, cols, chn = img.shape
cv2.imwrite('./Opencv/out.jpg', img)

# 分别获取 R,G,B三通道的值
blue = img[:, :, 0]
green = img[:, :, 1]
red = img[:, :, 2]
print(blue, green, red)

# 将行为100到200、列150到250的像素区域设置为白色
img[100:200, 150:250, :] = 255
cv2.imshow("title", img)

# Esc退出
while True:
    key = cv2.waitKey(0)
    if key == 27:
        cv2.destroyAllWindows()
        break
