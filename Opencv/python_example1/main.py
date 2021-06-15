# This Python file uses the following encoding: utf-8
import os
import sys
from PyQt5 import QtGui
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QGridLayout, QApplication, QWidget, QMainWindow, QFileDialog, QDialog, QMessageBox
from mainForm import Ui_MainWindow
from utils import ImgUtils, ImgConversion


class PyQtMainEntry(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.version = '0.0.1'
        self.setupUi(self)
        self.setWindowTitle("镜头矫正工具")
        self.setWindowIcon(QIcon('./icon.ico'))

        # Action监听事件
        self.actionOpen.triggered.connect(self.openFile)
        self.actionSave.triggered.connect(self.saveFile)
        self.actionAbout.triggered.connect(self.openAbout)

        self.imgPixmap = None
        self.imgPixmapProxy = None
        self.imgCv = None
        self.imgPixmapProxyList = None
        self.flashLabelImg(self.imgPixmapProxy)

    def btnAClicked(self):
        print("btnAClicked")

    def openFile(self):
        fileName, fileType = QFileDialog.getOpenFileName(
            self, "选取图片文件", os.getcwd(),
            "JPEG(*.JPG;*.JPEG;*.JPE);;PNG(*.PNG);;所有格式(*.*)")
        print("openfile: '" + fileName + "'  '" + fileType + "'")
        if fileName == '':
            return
        # 处理图像并刷新显示
        self.imgPixmap = QtGui.QPixmap(fileName)
        self.imgPixmapProxy = self.generateProxyImg(self.imgPixmap)
        self.imgCv = ImgConversion.qtpixmapToCvimg(self.imgPixmapProxy)
        self.imgPixmapProxyList = self.vignettingImgAll(self.imgCv)
        self.flashLabelImg(self.imgPixmapProxy)

    def saveFile(self):
        if self.imgPixmap is None:
            return
        fileName, fileType = QFileDialog.getSaveFileName(
            self, "另存为图片文件", os.getcwd(),
            "JPEG(*.JPG;*.JPEG;*.JPE);;PNG(*.PNG)")
        print("saveFile: '" + fileName + "'  '" + fileType + "'")
        if fileName == '':
            return
        # 读取当前参数 处理原图片 保存
        vignettingValue = self.horizontalSlider_vignetting.value()
        cvimg = ImgConversion.qtpixmapToCvimg(self.imgPixmap)
        cvimgResult = ImgUtils.vignettingImg(cvimg, vignettingValue / 20)
        ImgUtils.saveImg(fileName, cvimgResult)

    def openAbout(self):
        msgList = [
            "镜头矫正工具", "", "版本：v{0}".format(self.version), "小组：第Pi小组",
            "组员：王磊 李和兴 李昕辰", "完成日期：2021/6/15"
        ]
        QMessageBox.information(self, '关于', '\n'.join(msgList))

    # 预处理所有的图像
    def vignettingImgAll(self, cvimg):
        imgPixmapList = list()
        for i in range(-10, 11):
            cvimgResult = ImgUtils.vignettingImg(self.imgCv, i / 20)
            imgPixmapList.append(ImgConversion.cvimgToQtpixmap(cvimgResult))
        return imgPixmapList

    # 生成图像代理文件
    def generateProxyImg(self, pixmap):
        labelSize = self.label_img.size()
        imgSize = pixmap.size()
        if imgSize.height() >= imgSize.width():
            return pixmap.scaledToHeight(labelSize.height())
        else:
            return pixmap.scaledToWidth(labelSize.width())

    # 刷新图片显示label
    def flashLabelImg(self, pixmap):
        if pixmap is None:
            self.label_img.setText("未打开图片")
            return
        self.label_img.setPixmap(pixmap)

    ## 滑块调整事件
    def twistValueChanged(self, value):
        self.label_twist_value.setText(self.formatStrValue(value))

    def vignettingValueChanged(self, value):
        # 更改数值显示
        self.label_vignetting_value.setText(self.formatStrValue(value))
        # 展示预处理好的图像
        if self.imgPixmapProxyList is not None:
            self.flashLabelImg(self.imgPixmapProxyList[value + 10])

    # 格式化滑条显示值
    def formatStrValue(self, value):
        if value > 0:
            return '+' + str(value)
        else:
            return str(value)


class AboutDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("关于")
        self.setGeometry(400, 400, 300, 260)

        self.mainLayout = QGridLayout()
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PyQtMainEntry()
    window.show()
    sys.exit(app.exec_())
