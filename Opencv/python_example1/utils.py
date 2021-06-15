import os
import cv2
import numpy as np
import math
from PyQt5.QtGui import QImage, QPixmap


class ImgUtils():
    # 亮度 每个像素所有通道都加上b
    def contrastImg(cvimg, c, b):
        rows, cols, chunnel = cvimg.shape
        # np.zeros(img1.shape, dtype=uint8)
        blank = np.zeros([rows, cols, chunnel], cvimg.dtype)
        # dst = src1 * alpha + src2 * beta + gamma
        dst = cv2.addWeighted(cvimg, c, blank, 1 - c, b)
        return dst

    # 计算两二维点之间距离
    def dist(a, b):
        return math.sqrt(pow((a[0] - b[0]), 2) + pow((a[1] - b[1]), 2))

    # 计算图像中心点
    def centerPoint(cvimg):
        rows, cols, chunnel = cvimg.shape
        return [int(rows / 2), int(cols / 2)]

    # 暗角处理
    def vignettingImg(cvimgOriginal, weight):
        cvimg = np.copy(cvimgOriginal)
        rows, cols, chunnel = cvimg.shape
        # 中心点
        center = ImgUtils.centerPoint(cvimg)
        # 最大半径 即圈住图像的最小圆半径
        maxRadian = ImgUtils.dist([0, 0], center)
        # 最小半径 即约定范围
        minRadian = maxRadian * (1 - abs(weight))
        # 权重正值标记 权重为正减淡 为负加深
        if weight >= 0:
            for r in range(rows):
                for c in range(cols):
                    # 当前距中心点距离
                    tempDist = ImgUtils.dist([r, c], center)
                    # 验证约定范围
                    if tempDist > minRadian:
                        # 标准化 后得到点的权重值 (1 - 2)
                        tempWeight = 1 + (tempDist - minRadian) / (
                            maxRadian - minRadian) * abs(weight)
                        # 遍历防止越过 255 最大值
                        for i in [0, 1, 2]:
                            temp = cvimg[r, c, i] * tempWeight
                            if temp > 255:
                                cvimg[r, c, i] = 255
                            else:
                                cvimg[r, c, i] = temp
        else:
            for r in range(rows):
                for c in range(cols):
                    tempDist = ImgUtils.dist([r, c], center)
                    if tempDist > minRadian:
                        # 标准化 后得到点的反向权重值 (0 - 1)
                        tempWeight = 1 - (tempDist - minRadian) / (
                            maxRadian - minRadian) * abs(weight)
                        cvimg[r, c] = cvimg[r, c] * [
                            tempWeight, tempWeight, tempWeight
                        ]
        return cvimg

    def saveImg(filename, cvimg):
        cv2.imwrite(filename, cvimg)


class ImgConversion():
    def qtpixmapToCvimg(qtpixmap):
        qimg = qtpixmap.toImage()
        temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
        temp_shape += (4, )
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
        result = result[..., :3]
        return result

    def cvimgToQtpixmap(cvimg):
        height, width, depth = cvimg.shape
        cvimg = cv2.cvtColor(cvimg, cv2.COLOR_BGR2RGB)
        cvimg = QImage(cvimg.data, width, height, width * depth,
                       QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(cvimg)
        return pixmap


# Test
# img = cv2.imread('./v2.jpg')

# dst = ImgUtils.vignetting_img(img, (10 / 20))
# cv2.imshow('img', img)
# cv2.imshow('dst', dst)
# cv2.waitKey(0)
