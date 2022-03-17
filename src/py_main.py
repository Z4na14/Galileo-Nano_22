import sys

import matplotlib as matplotlib
import openpyxl as excel
import PyQt5

from PyQt5.QtWidgets import QApplication, QMainWindow, qApp
from PyQt5.QtCore import Qt, QEvent, QObject
from ui_main import Ui_MainWindow

class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        qApp.installEventFilter(self)
        self.setupUi(self)
        self.activar.clicked.connect(self.activar())


        self.show()
    def activar(self):
        self.desactivar.setEnabled(True)
        self.activar.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MyMainWindow()
    GUI.show()
    sys.exit(app.exec_())