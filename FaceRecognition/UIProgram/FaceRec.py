# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FaceRec.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1250, 800)
        MainWindow.setMinimumSize(QtCore.QSize(1250, 800))
        MainWindow.setMaximumSize(QtCore.QSize(1250, 800))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/人脸识别.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(0, 0, 1251, 101))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        self.label.setGeometry(QtCore.QRect(370, 0, 531, 81))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(self.frame_2)
        self.line.setGeometry(QtCore.QRect(0, 80, 1251, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily("华文行楷")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.frame_2)
        self.lcdNumber.setGeometry(QtCore.QRect(1050, 40, 191, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lcdNumber.setPalette(palette)
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lcdNumber.setDigitCount(8)
        self.lcdNumber.setObjectName("lcdNumber")
        self.Mainframe = QtWidgets.QFrame(self.centralwidget)
        self.Mainframe.setGeometry(QtCore.QRect(0, 100, 1251, 701))
        self.Mainframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Mainframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Mainframe.setObjectName("Mainframe")
        self.frame = QtWidgets.QFrame(self.Mainframe)
        self.frame.setGeometry(QtCore.QRect(0, 0, 340, 700))
        self.frame.setStyleSheet("")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.groupBox = QtWidgets.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 321, 691))
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 40, 301, 641))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(10, 0, 10, 20)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.infoEntryBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.infoEntryBtn.sizePolicy().hasHeightForWidth())
        self.infoEntryBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.infoEntryBtn.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/基础数据录入_编辑录入操作_jurassic.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.infoEntryBtn.setIcon(icon1)
        self.infoEntryBtn.setIconSize(QtCore.QSize(40, 40))
        self.infoEntryBtn.setObjectName("infoEntryBtn")
        self.verticalLayout.addWidget(self.infoEntryBtn)
        self.faceRecBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.faceRecBtn.sizePolicy().hasHeightForWidth())
        self.faceRecBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.faceRecBtn.setFont(font)
        self.faceRecBtn.setIcon(icon)
        self.faceRecBtn.setIconSize(QtCore.QSize(40, 40))
        self.faceRecBtn.setObjectName("faceRecBtn")
        self.verticalLayout.addWidget(self.faceRecBtn)
        self.dataManageBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dataManageBtn.sizePolicy().hasHeightForWidth())
        self.dataManageBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.dataManageBtn.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/验收数据管理.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.dataManageBtn.setIcon(icon2)
        self.dataManageBtn.setIconSize(QtCore.QSize(35, 35))
        self.dataManageBtn.setObjectName("dataManageBtn")
        self.verticalLayout.addWidget(self.dataManageBtn)
        self.recRecordBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.recRecordBtn.sizePolicy().hasHeightForWidth())
        self.recRecordBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.recRecordBtn.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/信息_记录.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.recRecordBtn.setIcon(icon3)
        self.recRecordBtn.setIconSize(QtCore.QSize(30, 30))
        self.recRecordBtn.setObjectName("recRecordBtn")
        self.verticalLayout.addWidget(self.recRecordBtn)
        self.aboutBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.aboutBtn.sizePolicy().hasHeightForWidth())
        self.aboutBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.aboutBtn.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/关于我们.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.aboutBtn.setIcon(icon4)
        self.aboutBtn.setIconSize(QtCore.QSize(40, 40))
        self.aboutBtn.setObjectName("aboutBtn")
        self.verticalLayout.addWidget(self.aboutBtn)
        self.exitBtn = QtWidgets.QPushButton(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.exitBtn.sizePolicy().hasHeightForWidth())
        self.exitBtn.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("华文楷体")
        font.setPointSize(16)
        self.exitBtn.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/ui_imgs/icons/退出.png"), QtGui.QIcon.Active, QtGui.QIcon.On)
        self.exitBtn.setIcon(icon5)
        self.exitBtn.setIconSize(QtCore.QSize(40, 40))
        self.exitBtn.setObjectName("exitBtn")
        self.verticalLayout.addWidget(self.exitBtn)
        self.show_frame = QtWidgets.QFrame(self.Mainframe)
        self.show_frame.setGeometry(QtCore.QRect(340, 0, 910, 700))
        self.show_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.show_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.show_frame.setObjectName("show_frame")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "人脸识别与信息管理系统 V1.0"))
        self.label.setText(_translate("MainWindow", "鸡只个体健康状况监测系统"))
        self.label_2.setText(_translate("MainWindow", "SRTP项目软件"))
        self.groupBox.setTitle(_translate("MainWindow", "操作列表"))
        self.infoEntryBtn.setText(_translate("MainWindow", "鸡脸信息录入"))
        self.faceRecBtn.setText(_translate("MainWindow", "鸡脸识别"))
        self.dataManageBtn.setText(_translate("MainWindow", "数据管理"))
        self.recRecordBtn.setText(_translate("MainWindow", "识别记录"))
        self.aboutBtn.setText(_translate("MainWindow", "关于"))
        self.exitBtn.setText(_translate("MainWindow", "退出"))
import img_source_rc
