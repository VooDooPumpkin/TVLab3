import sys
import math
import combinatorics
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

        # connects
        self.ui.chooseFormula.activated[int].connect(self.formulaChanged)

    #Смена формулы
    def formulaChanged(self, idx):
        #show widgets for Bernuli
        if idx == 0:
            # show widgets for Bernuli
            self.ui.groupBern.show()
            self.ui.label_6.show()
            self.ui.label_7.show()
            self.ui.label_8.show()
            self.ui.label_9.show()
            self.ui.label_10.show()
            self.ui.bernP.show()
            self.ui.bernN.show()
            self.ui.bernM.show()
            self.ui.bernM1.show()
            self.ui.bernM2.show()
            # hide widgets for Polinomal
            self.ui.label_11.hide()
            self.ui.label_12.hide()
            self.ui.label_13.hide()
            self.ui.label_14.hide()
            self.ui.poliN.hide()
            self.ui.poliK.hide()
            self.ui.poliM.hide()
            self.ui.poliP.hide()

        #show widgets for Polinomal
        else:
            # hide widgets for Bernuli
            self.ui.groupBern.hide()
            self.ui.groupBern.hide()
            self.ui.label_6.hide()
            self.ui.label_7.hide()
            self.ui.label_8.hide()
            self.ui.label_9.hide()
            self.ui.label_10.hide()
            self.ui.bernP.hide()
            self.ui.bernN.hide()
            self.ui.bernM.hide()
            self.ui.bernM1.hide()
            self.ui.bernM2.hide()
            # show widgets for Polinomal
            self.ui.label_11.show()
            self.ui.label_12.show()
            self.ui.label_13.show()
            self.ui.label_14.show()
            self.ui.poliN.show()
            self.ui.poliK.show()
            self.ui.poliM.show()
            self.ui.poliP.show()



# show window
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())