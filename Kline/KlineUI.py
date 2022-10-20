import os
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setWindowTitle('加载本地网页的例子')
        self.setGeometry(5, 30, 2000, 1200)
        self.browser = QWebEngineView()
        # #加载外部的web界面
        url = os.getcwd() + os.path.sep + 'kline_volume_signal.html'
        print(url)
        self.browser.load(QUrl.fromLocalFile(url))
        self.setCentralWidget(self.browser)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exit(app.exec_())
