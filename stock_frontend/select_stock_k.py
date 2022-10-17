# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'select_stock_k.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_SelectStockKgraphWindow(object):
    def setupUi(self, SelectStockKgraphWindow):
        SelectStockKgraphWindow.setObjectName("SelectStockKgraphWindow")
        SelectStockKgraphWindow.resize(1148, 769)
        SelectStockKgraphWindow.setToolTip("")
        SelectStockKgraphWindow.setStatusTip("")
        self.centralwidget = QtWidgets.QWidget(SelectStockKgraphWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonRefresh = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRefresh.setGeometry(QtCore.QRect(1010, 10, 131, 32))
        self.pushButtonRefresh.setObjectName("pushButtonRefresh")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(160, 10, 841, 34))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton1min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton1min.setMaximumSize(QtCore.QSize(70, 16777215))
        self.pushButton1min.setStyleSheet("")
        self.pushButton1min.setObjectName("pushButton1min")
        self.horizontalLayout.addWidget(self.pushButton1min)
        self.pushButton5min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton5min.setStyleSheet("")
        self.pushButton5min.setObjectName("pushButton5min")
        self.horizontalLayout.addWidget(self.pushButton5min)
        self.pushButton15min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton15min.setStyleSheet("")
        self.pushButton15min.setObjectName("pushButton15min")
        self.horizontalLayout.addWidget(self.pushButton15min)
        self.pushButton30min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton30min.setStyleSheet("")
        self.pushButton30min.setObjectName("pushButton30min")
        self.horizontalLayout.addWidget(self.pushButton30min)
        self.pushButton60min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton60min.setStyleSheet("")
        self.pushButton60min.setObjectName("pushButton60min")
        self.horizontalLayout.addWidget(self.pushButton60min)
        self.pushButton120min = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton120min.setStyleSheet("")
        self.pushButton120min.setObjectName("pushButton120min")
        self.horizontalLayout.addWidget(self.pushButton120min)
        self.pushButtonDay = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonDay.setStyleSheet("")
        self.pushButtonDay.setObjectName("pushButtonDay")
        self.horizontalLayout.addWidget(self.pushButtonDay)
        self.pushButtonMonth = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonMonth.setStyleSheet("")
        self.pushButtonMonth.setObjectName("pushButtonMonth")
        self.horizontalLayout.addWidget(self.pushButtonMonth)
        self.label_TimeStatus = QtWidgets.QLabel(self.centralwidget)
        self.label_TimeStatus.setGeometry(QtCore.QRect(880, 0, 41, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.label_TimeStatus.setFont(font)
        self.label_TimeStatus.setText("")
        self.label_TimeStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.label_TimeStatus.setObjectName("label_TimeStatus")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(430, 50, 321, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setAlignment(QtCore.Qt.AlignCenter)
        self.label_17.setObjectName("label_17")
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 100, 1131, 151))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridLayout.addWidget(self.lineEdit_2, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 4, 1, 1)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.gridLayout.addWidget(self.lineEdit_5, 0, 5, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 6, 1, 1)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.gridLayout.addWidget(self.lineEdit_3, 0, 7, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 8, 1, 1)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.gridLayout.addWidget(self.lineEdit_4, 0, 9, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 1, 0, 1, 1)
        self.lineEdit_10 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.gridLayout.addWidget(self.lineEdit_10, 1, 1, 1, 1)
        self.label_9 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 1, 2, 1, 1)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.gridLayout.addWidget(self.lineEdit_6, 1, 3, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 1, 4, 1, 1)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.gridLayout.addWidget(self.lineEdit_8, 1, 5, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 1, 6, 1, 1)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.gridLayout.addWidget(self.lineEdit_7, 1, 7, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 1, 8, 1, 1)
        self.lineEdit_9 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.gridLayout.addWidget(self.lineEdit_9, 1, 9, 1, 1)
        self.label_12 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 2, 0, 1, 1)
        self.lineEdit_15 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_15.setObjectName("lineEdit_15")
        self.gridLayout.addWidget(self.lineEdit_15, 2, 1, 1, 1)
        self.label_14 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_14.setObjectName("label_14")
        self.gridLayout.addWidget(self.label_14, 2, 2, 1, 1)
        self.lineEdit_11 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_11.setObjectName("lineEdit_11")
        self.gridLayout.addWidget(self.lineEdit_11, 2, 3, 1, 1)
        self.label_13 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 2, 4, 1, 1)
        self.lineEdit_13 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_13.setObjectName("lineEdit_13")
        self.gridLayout.addWidget(self.lineEdit_13, 2, 5, 1, 1)
        self.label_15 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_15.setObjectName("label_15")
        self.gridLayout.addWidget(self.label_15, 2, 6, 1, 1)
        self.lineEdit_12 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_12.setObjectName("lineEdit_12")
        self.gridLayout.addWidget(self.lineEdit_12, 2, 7, 1, 1)
        self.label_16 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_16.setObjectName("label_16")
        self.gridLayout.addWidget(self.label_16, 2, 8, 1, 1)
        self.lineEdit_14 = QtWidgets.QLineEdit(self.layoutWidget1)
        self.lineEdit_14.setObjectName("lineEdit_14")
        self.gridLayout.addWidget(self.lineEdit_14, 2, 9, 1, 1)
        self.pushButtonReturn = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonReturn.setGeometry(QtCore.QRect(10, 10, 141, 31))
        self.pushButtonReturn.setObjectName("pushButtonReturn")
        SelectStockKgraphWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SelectStockKgraphWindow)
        QtCore.QMetaObject.connectSlotsByName(SelectStockKgraphWindow)

    def retranslateUi(self, SelectStockKgraphWindow):
        _translate = QtCore.QCoreApplication.translate
        SelectStockKgraphWindow.setWindowTitle(_translate("SelectStockKgraphWindow", "交易信息"))
        self.pushButtonRefresh.setText(_translate("SelectStockKgraphWindow", "设置"))
        self.pushButton1min.setText(_translate("SelectStockKgraphWindow", "1分钟"))
        self.pushButton5min.setText(_translate("SelectStockKgraphWindow", "5分钟"))
        self.pushButton15min.setText(_translate("SelectStockKgraphWindow", "15分钟"))
        self.pushButton30min.setText(_translate("SelectStockKgraphWindow", "30分钟"))
        self.pushButton60min.setText(_translate("SelectStockKgraphWindow", "60分钟"))
        self.pushButton120min.setText(_translate("SelectStockKgraphWindow", "120分钟"))
        self.pushButtonDay.setText(_translate("SelectStockKgraphWindow", "日"))
        self.pushButtonMonth.setText(_translate("SelectStockKgraphWindow", "月"))
        self.label_17.setText(_translate("SelectStockKgraphWindow", "********股票名称********"))
        self.label_2.setText(_translate("SelectStockKgraphWindow", "时刻"))
        self.label_3.setText(_translate("SelectStockKgraphWindow", "开盘价"))
        self.label_6.setText(_translate("SelectStockKgraphWindow", "收盘价"))
        self.label_4.setText(_translate("SelectStockKgraphWindow", "最高价"))
        self.label_5.setText(_translate("SelectStockKgraphWindow", "最低价"))
        self.label_7.setText(_translate("SelectStockKgraphWindow", "MAS"))
        self.label_9.setText(_translate("SelectStockKgraphWindow", "MA10"))
        self.label_8.setText(_translate("SelectStockKgraphWindow", "MA30"))
        self.label_10.setText(_translate("SelectStockKgraphWindow", "MA60"))
        self.label_11.setText(_translate("SelectStockKgraphWindow", "MA120"))
        self.label_12.setText(_translate("SelectStockKgraphWindow", "MA240"))
        self.label_14.setText(_translate("SelectStockKgraphWindow", "MA360"))
        self.label_13.setText(_translate("SelectStockKgraphWindow", "涨跌"))
        self.label_15.setText(_translate("SelectStockKgraphWindow", "涨幅"))
        self.label_16.setText(_translate("SelectStockKgraphWindow", "成交量"))
        self.pushButtonReturn.setText(_translate("SelectStockKgraphWindow", "返回主界面"))