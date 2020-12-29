import numpy
import cv2

img = cv2.imread("./Opencv/img.jpg")

print(type(img))

print(img.ndim)     # 维度数
print(img.shape)    # 每一维度个数
print(img.dtype)    # 数据类型
print(img.size)     # 大小


img = img[::-1, ::-1, ::-1]

cv2.imshow("Demo", img)
cv2.waitKey(0)
cv2.destroyAllWindows()


# 完成进制转换 1.D转H D转B

