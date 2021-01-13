import time

from PyQt5.QtCore import QThread, pyqtSignal, QDateTime
from PyQt5.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QPushButton, QVBoxLayout


class BackendThread(QThread):
    update_date = pyqtSignal(dict)

    def run(self):
        while True:
            date = QDateTime.currentDateTime()
            currentTime = date.toString("yyyy-MM-dd hh:mm:ss")
            self.update_date.emit({"1":str(currentTime)})
            time.sleep(1)


class Window(QMainWindow):
    windowList = []

    def page_setup(self, title):
        self.setWindowTitle(title)

        ###### 创建界面 ######
        self.centralwidget = QWidget()
        self.setCentralWidget(self.centralwidget)
        self.Layout = QVBoxLayout(self.centralwidget)

        # 设置顶部三个按钮
        self.topwidget = QWidget()
        self.Layout.addWidget(self.topwidget)
        self.buttonLayout = QHBoxLayout(self.topwidget)

        self.pushButton1 = QPushButton()
        self.pushButton1.setText("主界面")
        self.buttonLayout.addWidget(self.pushButton1)

        self.pushButton2 = QPushButton()
        self.pushButton2.setText("电池")
        self.buttonLayout.addWidget(self.pushButton2)

        self.pushButton3 = QPushButton()
        self.pushButton3.setText("发动机")
        self.buttonLayout.addWidget(self.pushButton3)
        self.but_name_list = []
        self.but_list = []
        for i, name_list in enumerate(self.names):
            self.topwidget = QWidget()
            self.Layout.addWidget(self.topwidget)
            self.buttonLayout = QHBoxLayout(self.topwidget)
            for j, name in enumerate(name_list):
                button = QPushButton()
                button.setText(name)
                # button.resize(100, 50)
                button.setToolTip(name)
                self.buttonLayout.addWidget(button)
                self.but_list.append(button)
                self.but_name_list.append(name)
        # 设置状态栏
        self.statusBar().showMessage("当前用户：bufan")

        # 窗口最大化
        self.showMaximized()