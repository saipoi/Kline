# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setting_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SettiingWindow(object):
    def setupUi(self, SettiingWindow):
        SettiingWindow.setObjectName("SettiingWindow")
        SettiingWindow.resize(450, 467)
        self.centralwidget = QtWidgets.QWidget(SettiingWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonSetting = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonSetting.setGeometry(QtCore.QRect(80, 400, 104, 32))
        self.pushButtonSetting.setObjectName("pushButtonSetting")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(80, 50, 282, 321))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEdit15k = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit15k.setObjectName("lineEdit15k")
        self.gridLayout.addWidget(self.lineEdit15k, 1, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit5k = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit5k.setObjectName("lineEdit5k")
        self.gridLayout.addWidget(self.lineEdit5k, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 3, 0, 1, 1)
        self.lineEdit30k = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit30k.setObjectName("lineEdit30k")
        self.gridLayout.addWidget(self.lineEdit30k, 2, 1, 1, 1)
        self.lineEdit60k = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEdit60k.setObjectName("lineEdit60k")
        self.gridLayout.addWidget(self.lineEdit60k, 3, 1, 1, 1)
        self.pushButtonReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(220, 400, 104, 32))
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        SettiingWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SettiingWindow)
        QtCore.QMetaObject.connectSlotsByName(SettiingWindow)

    def retranslateUi(self, SettiingWindow):
        _translate = QtCore.QCoreApplication.translate
        SettiingWindow.setWindowTitle(_translate("SettiingWindow", "设置"))
        self.pushButtonSetting.setText(_translate("SettiingWindow", "导出K-线图"))
        self.label_2.setText(_translate("SettiingWindow", "开始日期"))
        self.label_3.setText(_translate("SettiingWindow", "结束日期"))
        self.label.setText(_translate("SettiingWindow", "股票代码"))
        self.label_6.setText(_translate("SettiingWindow", "时间间隔"))
        self.pushButtonReturn.setText(_translate("SettiingWindow", "返回主界面"))