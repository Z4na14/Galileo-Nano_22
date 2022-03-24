import sys

import matplotlib as matplotlib
import openpyxl as excel

from PyQt5.QtWidgets import QApplication, QMainWindow, qApp, QPushButton
from pruebas_ui import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow, QPushButton):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow
        self.ui.setupUi(self)
        self.ui.activar.clicked.connect(self.ui.activar)

        self.ui.show()
    def activar(self):
        self.ui.desactivar.setEnabled(True)
        self.ui.activar.setEnabled(False)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = MyMainWindow()
    GUI.show()
    sys.exit(app.exec_())