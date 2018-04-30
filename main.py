import sys
import math
import combinatorics as combi
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QDialog, QApplication, QMessageBox
from mainwindow import Ui_Dialog

#Solving functions

#Bernuli formula
def bernuli(p, n, m2, m1 = 0):
    res = 0
    for i in range(m1, m2):
        res += combi.combinatorics.combiNoRep(n, i) * p ** i * (1 - p) ** (n - i)
    return res

#Polinomal formula
def polinomal(n, k, arrayM, arrayP):
    res = combi.combinatorics.permWithRep(n, arrayM)
    for i in range(k):
        res*= float(arrayP[i]) ** int(arrayM[i])
    return res

#Integral Muavra formula
def integralMuavra(n, p, m1, m2, segments):
    q = 1 - p
    x1 = (m1 - n*p)/math.sqrt(n*p*q)
    x2 = (m2 - n*p)/math.sqrt(n*p*q)
    h = (x2 - x1) / segments
    res = 1/math.sqrt(2*math.pi)
    integ = math.exp(-(x1**2/2))+ math.exp(-(x2**2/2))
    for i in range(1,segments):
        if (i%2 == 0):
            integ += 2*(math.exp(-((x1 + i*h)**2/2)))
        else:
            integ += 4*(math.exp(-((x1 + i * h)**2/2)))
    integ *= h/3
    res *= integ
    return res

# window
class AppWindow(QDialog):

    curForm = 0

    # prepare window
    def __init__(self):

        # init window
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        #widgets init
        self.ui.bern1.setChecked(True)
        self.ui.showBernRes.hide()
        self.formulaChanged(0)
        self.bernOneBorder()

        # set validators
        reg_ex = QRegExp("(\d{1}([\.]{1}\d{1,5})? {1})*")
        reg_ex2 = QRegExp("(\d{1,5} {1})*")
        validatorArrayM = QRegExpValidator(reg_ex2, self.ui.poliM)
        validatorArrayP = QRegExpValidator(reg_ex, self.ui.poliP)
        self.ui.poliM.setValidator(validatorArrayM)
        self.ui.poliP.setValidator(validatorArrayP)

        # connects
        self.ui.chooseFormula.activated[int].connect(self.formulaChanged)
        self.ui.bern1.toggled[bool].connect(self.bernOneBorder)
        self.ui.bern2.toggled[bool].connect(self.bernOneBorder)
        self.ui.bern3.toggled[bool].connect(self.bernOneBorder)
        self.ui.bern4.toggled[bool].connect(self.bernTwoBorders)
        self.ui.getResult.clicked[bool].connect(self.getRes)

    #Change widgets for selected formula
    def formulaChanged(self, idx):
        self.curForm = idx
        #show widgets for Bernuli
        if idx == 0:
            # show widgets for Bernuli
            self.ui.groupBern.show()
            self.ui.label_6.show()
            self.ui.label_7.show()
            self.ui.label_8.show()
            self.ui.bernP.show()
            self.ui.bernN.show()
            self.ui.bernM.show()
            self.ui.label_9.show()
            self.ui.label_10.show()
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
            self.ui.showBernRes.hide()

        #show widgets for Polinomal
        elif idx == 1:
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
            self.ui.showBernRes.hide()
            # show widgets for Polinomal
            self.ui.label_11.show()
            self.ui.label_12.show()
            self.ui.label_13.show()
            self.ui.label_14.show()
            self.ui.poliN.show()
            self.ui.poliK.show()
            self.ui.poliM.show()
            self.ui.poliP.show()
        elif idx == 2:
            # show widgets for Integral Muavra
            self.ui.FormulaView.setPixmap(QPixmap('Muavra.jpg').scaled(QSize(600, 72)))
            self.ui.label_6.show()
            self.ui.label_7.show()
            self.ui.bernP.show()
            self.ui.bernN.show()
            self.ui.label_9.show()
            self.ui.label_10.show()
            self.ui.bernM1.show()
            self.ui.bernM2.show()
            self.ui.showBernRes.show()
            # hide widgets for Polinomal and Bernuli
            self.ui.groupBern.hide()
            self.ui.label_8.hide()
            self.ui.bernM.hide()
            self.ui.label_11.hide()
            self.ui.label_12.hide()
            self.ui.label_13.hide()
            self.ui.label_14.hide()
            self.ui.poliN.hide()
            self.ui.poliK.hide()
            self.ui.poliM.hide()
            self.ui.poliP.hide()

    #selected event with one border
    def bernOneBorder(self):
        self.ui.label_8.show()
        self.ui.bernM.show()
        self.ui.label_9.hide()
        self.ui.label_10.hide()
        self.ui.bernM1.hide()
        self.ui.bernM2.hide()

    #selected event with two borders
    def bernTwoBorders(self):
        self.ui.label_8.hide()
        self.ui.bernM.hide()
        self.ui.label_9.show()
        self.ui.label_10.show()
        self.ui.bernM1.show()
        self.ui.bernM2.show()

    #Counting by Bernuli formula
    def solveBern(self):
        if self.ui.bern1.isChecked():
            p = self.ui.bernP.value()
            n = self.ui.bernN.value()
            m = self.ui.bernM.value()
            self.ui.textResult.setText(str(bernuli(p, n, int(m) + 1, m)))
        elif self.ui.bern2.isChecked():
            p = self.ui.bernP.value()
            n = self.ui.bernN.value()
            m = self.ui.bernM.value()
            self.ui.textResult.setText(str(bernuli(p, n, m)))
        elif self.ui.bern3.isChecked():
            p = self.ui.bernP.value()
            n = self.ui.bernN.value()
            m = self.ui.bernM.value()
            self.ui.textResult.setText(str(bernuli(p, n, n + 1, int(m))))
        elif self.ui.bern4.isChecked():
            p = self.ui.bernP.value()
            n = self.ui.bernN.value()
            m1 = self.ui.bernM1.value()
            m2 = self.ui.bernM2.value()
            self.ui.textResult.setText(str(bernuli(p, n, m2 + 1, m1)))

    # Counting by Polinomal formula
    def solvePoli(self):
        n = self.ui.poliN.value()
        k = self.ui.poliK.value()
        string = self.ui.poliM.text()
        arrayM = string.split()
        string = self.ui.poliP.text()
        arrayP = string.split()
        self.ui.textResult.setText(str(polinomal(n, k, arrayM, arrayP)))

    def solveIntegralMuavra(self):
        p = self.ui.bernP.value()
        n = self.ui.bernN.value()
        m1 = self.ui.bernM1.value()
        m2 = self.ui.bernM2.value()
        resMuavra = integralMuavra(n, p, m1, m2, 100)
        string = "Результат по интегральной теореме Муавра - Лапласа: \n" + str(resMuavra)
        if self.ui.showBernRes.isChecked():
            resBern = bernuli(p, n, m2 + 1, m1)
            string += "\nРезультат по формуле Бернулли: \n" + str(resBern)
            string += "\nРазница между результатами:\n " + str(abs(resMuavra - resBern))
        self.ui.textResult.setText(string)


    #check data from widgets and get result
    def getRes(self):
        if self.curForm == 0:
            # check for errors
            if self.ui.bernP.value() > 1 or self.ui.bernP.value() < 0:
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Вероятность события не может быть больше 1 или меньше 0!')
                msg.exec_()
            elif self.ui.bernM.value() > self.ui.bernN.value() or self.ui.bernM1.value() > self.ui.bernN.value() or self.ui.bernM2.value() > self.ui.bernN.value():
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Количество появлений события не может быть больше количества испытаний!')
                msg.exec_()
            else:
                self.solveBern()
        elif self.curForm == 1:
            #check for errors
            string = self.ui.poliM.text()
            arrayM = string.split()
            string = self.ui.poliP.text()
            arrayP = string.split()
            #check probabilities
            probs = True
            for i in range(len(arrayP)):
                if float(arrayP[i]) > 1 or float(arrayP[i]) < 0:
                    probs = False
            # sum M
            sumM = 0
            for i in range(len(arrayM)):
                sumM += int(arrayM[i])
            if sumM != self.ui.poliN.value():
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Количество появлений событий должно быть равным количеству испытаний!')
                msg.exec_()
            elif len(arrayP) != len(arrayM):
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Количество вероятностей появлений событий должно быть равным количеству появлений событий!')
                msg.exec_()
            elif probs == False:
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Вероятность события не может быть больше 1 или меньше 0!')
                msg.exec_()
            else:
                self.solvePoli()
        elif self.curForm == 2:
            # check for errors
            if self.ui.bernP.value() > 1 or self.ui.bernP.value() < 0:
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Вероятность события не может быть больше 1 или меньше 0!')
                msg.exec_()
            elif self.ui.bernM.value() > self.ui.bernN.value() or self.ui.bernM1.value() > self.ui.bernN.value() or self.ui.bernM2.value() > self.ui.bernN.value():
                # show error
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText('Количество появлений события не может быть больше количества испытаний!')
                msg.exec_()
            else:
                self.solveIntegralMuavra()










# show window
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())