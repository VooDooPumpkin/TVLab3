import sys
import math
import combinatorics.py
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from mainwindow import Ui_Dialog

# window
class AppWindow(QDialog):

    # prepare window
    def __init__(self):

        # init window
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

# show window
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())