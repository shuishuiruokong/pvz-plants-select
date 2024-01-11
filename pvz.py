from PySide6 import QtGui
from PySide6.QtCore import (QMetaObject, QRect, Qt)
from PySide6.QtGui import (QIcon, QPainterPath, QPainter, QPixmap)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
                               QPushButton, QStatusBar, QWidget, QCheckBox)
import sys
import random
import os


# 解压文件
def get_resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(700, 500)

        icon_path = "resource/pictures/icon.png"
        # 绘制圆形窗口图标
        pixmap = QPixmap(icon_path).scaled(32, 32)  # 缩放图标大小
        circle_pixmap = QPixmap(pixmap.size())
        circle_pixmap.fill(Qt.transparent)

        painter = QPainter(circle_pixmap)
        painter.setRenderHint(QPainter.Antialiasing, True)
        path = QPainterPath()
        path.addEllipse(0, 0, pixmap.width(), pixmap.height())
        painter.setClipPath(path)
        painter.drawPixmap(0, 0, pixmap)
        painter.end()
        MainWindow.setWindowIcon(circle_pixmap)  # 图标

        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")

        self.background_p = QLabel(self.centralwidget)
        self.background_p.setGeometry(QRect(0, 0, MainWindow.width(), MainWindow.height()))
        self.background_p.setPixmap(QPixmap(get_resource_path("resource/pictures/background.jpg")))
        self.background_p.lower()

        # 接收期望抽取植物的数量
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(200, 55, 71, 20))
        self.lineEdit.setStyleSheet("background-color: transparent; border: none;")

        self.label0 = QLabel(self.centralwidget)
        self.label0.setGeometry(QRect(185, 40, 100, 50))
        self.pix = QtGui.QPixmap(get_resource_path(get_resource_path('resource/pictures/LineEdit.png'))).scaled(self.label0.size())
        self.label0.setPixmap(self.pix)
        self.label0.setStyleSheet("background-color: transparent;")
        self.lineEdit.raise_()

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(200, 130, 75, 24))
        self.pushButton.clicked.connect(MainWindow.choose)
        self.pushButton.setIcon(QIcon(get_resource_path(r'resource/pictures/开始.png')))
        self.pushButton.setIconSize(self.pushButton.size())
        self.pushButton.setStyleSheet("background-color: transparent;")

        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(150, 60, 91, 20))

        self.label_1 = QLabel(self.centralwidget)
        self.label_1.setObjectName(u"label_2")
        self.label_1.setGeometry(QRect(60, 170, 60, 71))

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_3")
        self.label_2.setGeometry(QRect(160, 170, 60, 71))

        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_4")
        self.label_3.setGeometry(QRect(260, 170, 60, 71))

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_5")
        self.label_4.setGeometry(QRect(360, 170, 60, 71))

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 280, 60, 71))

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 280, 60, 71))

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_8")
        self.label_7.setGeometry(QRect(260, 280, 60, 71))

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_9")
        self.label_8.setGeometry(QRect(360, 280, 60, 71))

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_11")
        self.label_9.setGeometry(QRect(60, 390, 60, 71))

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_12")
        self.label_10.setGeometry(QRect(160, 390, 60, 71))

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_12")
        self.label_11.setGeometry(QRect(260, 390, 60, 71))

        self.label_12 = QLabel(self.centralwidget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(360, 390, 60, 71))

        self.label_list = [self.label_1, self.label_2, self.label_3, self.label_4, self.label_5, self.label_6,
                           self.label_7, self.label_8, self.label_9, self.label_10, self.label_11, self.label_12]

        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.checkbox1 = QCheckBox("无夜间植物", self)
        self.checkbox1.setGeometry(QRect(120, 100, 100, 24))

        self.checkbox2 = QCheckBox("无进阶植物", self)
        self.checkbox2.setGeometry(QRect(270, 100, 100, 24))

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("植物盲盒")
        self.label.setText("")

    # retranslateUi


class m_window_analysis(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(m_window_analysis, self).__init__()
        self.setupUi(self)

    def choose(self):
        self.reset()
        num = int(self.lineEdit.text())  # 接收期望抽取植物的数量
        no_night_plants = self.checkbox1.isChecked()  # 判断是否选取夜间植物
        no_advanced_plants = self.checkbox2.isChecked()  # 判断是否选取进阶植物

        num_lst = [i for i in range(0, 49)]
        flag = 0
        night_plants_list = [9, 10, 11, 12, 13, 14, 16, 25, 26, 32, 36]  # 夜间植物编号
        advanced_plants_list = [41, 42, 43, 44, 45, 46, 47, 48]  # 进阶植物编号
        if no_night_plants:
            num_lst = [x for x in num_lst if x not in night_plants_list]
        if no_advanced_plants:
            num_lst = [x for x in num_lst if x not in advanced_plants_list]

        seed_list = random.sample(num_lst, num)  # 随机生成指定数量的植物编号
        seed_list.sort()
        for i in seed_list:
            i_path = r"resource/pictures/图层 " + str(i) + '.png'
            self.pix = QtGui.QPixmap(i_path).scaled(self.label_1.size())
            self.label_list[flag].setPixmap(self.pix)
            flag += 1

    def reset(self):
        self.label_1.setText(" ")
        self.label_2.setText(" ")
        self.label_3.setText(" ")
        self.label_4.setText(" ")
        self.label_5.setText(" ")
        self.label_6.setText(" ")
        self.label_7.setText(" ")
        self.label_8.setText(" ")
        self.label_9.setText(" ")
        self.label_10.setText(" ")
        self.label_11.setText(" ")
        self.label_12.setText(" ")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window1 = m_window_analysis()
    window1.show()
    app.exec_()
