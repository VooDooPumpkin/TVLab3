# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(512, 652)
        self.verticalLayout_13 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_13.setObjectName("verticalLayout_13")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setObjectName("label")
        self.verticalLayout_13.addWidget(self.label)
        self.chooseFormula = QtWidgets.QComboBox(Dialog)
        self.chooseFormula.setObjectName("chooseFormula")
        self.chooseFormula.addItem("")
        self.chooseFormula.addItem("")
        self.verticalLayout_13.addWidget(self.chooseFormula)
        self.FormulaView = QtWidgets.QLabel(Dialog)
        self.FormulaView.setText("")
        self.FormulaView.setObjectName("FormulaView")
        self.verticalLayout_13.addWidget(self.FormulaView)
        self.groupBern = QtWidgets.QGroupBox(Dialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBern.sizePolicy().hasHeightForWidth())
        self.groupBern.setSizePolicy(sizePolicy)
        self.groupBern.setMinimumSize(QtCore.QSize(400, 100))
        self.groupBern.setMaximumSize(QtCore.QSize(1900, 100))
        self.groupBern.setObjectName("groupBern")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.groupBern)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.bern1 = QtWidgets.QRadioButton(self.groupBern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bern1.sizePolicy().hasHeightForWidth())
        self.bern1.setSizePolicy(sizePolicy)
        self.bern1.setText("")
        self.bern1.setObjectName("bern1")
        self.horizontalLayout_4.addWidget(self.bern1)
        self.label_2 = QtWidgets.QLabel(self.groupBern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setMaximumSize(QtCore.QSize(100, 25))
        self.label_2.setBaseSize(QtCore.QSize(0, 0))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("Bernuli1.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_4.addWidget(self.label_2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_10.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.bern2 = QtWidgets.QRadioButton(self.groupBern)
        self.bern2.setText("")
        self.bern2.setObjectName("bern2")
        self.horizontalLayout_5.addWidget(self.bern2)
        self.label_3 = QtWidgets.QLabel(self.groupBern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMaximumSize(QtCore.QSize(100, 25))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("Bernuli2.jpg"))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem1)
        self.verticalLayout_10.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_8.addLayout(self.verticalLayout_10)
        self.verticalLayout_11 = QtWidgets.QVBoxLayout()
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.bern3 = QtWidgets.QRadioButton(self.groupBern)
        self.bern3.setText("")
        self.bern3.setObjectName("bern3")
        self.horizontalLayout_6.addWidget(self.bern3)
        self.label_4 = QtWidgets.QLabel(self.groupBern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMaximumSize(QtCore.QSize(100, 25))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("Bernuli3.jpg"))
        self.label_4.setScaledContents(True)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_6.addWidget(self.label_4)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.bern4 = QtWidgets.QRadioButton(self.groupBern)
        self.bern4.setText("")
        self.bern4.setObjectName("bern4")
        self.horizontalLayout_7.addWidget(self.bern4)
        self.label_5 = QtWidgets.QLabel(self.groupBern)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setMaximumSize(QtCore.QSize(150, 25))
        self.label_5.setText("")
        self.label_5.setPixmap(QtGui.QPixmap("Bernuli4.jpg"))
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_7.addWidget(self.label_5)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_8.addLayout(self.verticalLayout_11)
        self.verticalLayout_12.addLayout(self.horizontalLayout_8)
        self.verticalLayout_13.addWidget(self.groupBern)
        self.layout_Bernuli = QtWidgets.QVBoxLayout()
        self.layout_Bernuli.setObjectName("layout_Bernuli")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_6 = QtWidgets.QLabel(Dialog)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_5.addWidget(self.label_6)
        self.bernP = QtWidgets.QDoubleSpinBox(Dialog)
        self.bernP.setObjectName("bernP")
        self.verticalLayout_5.addWidget(self.bernP)
        self.layout_Bernuli.addLayout(self.verticalLayout_5)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_7 = QtWidgets.QLabel(Dialog)
        self.label_7.setObjectName("label_7")
        self.verticalLayout.addWidget(self.label_7)
        self.bernN = QtWidgets.QSpinBox(Dialog)
        self.bernN.setObjectName("bernN")
        self.verticalLayout.addWidget(self.bernN)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_8 = QtWidgets.QLabel(Dialog)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        self.bernM = QtWidgets.QSpinBox(Dialog)
        self.bernM.setObjectName("bernM")
        self.verticalLayout_2.addWidget(self.bernM)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.layout_Bernuli.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_9 = QtWidgets.QLabel(Dialog)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_3.addWidget(self.label_9)
        self.bernM1 = QtWidgets.QSpinBox(Dialog)
        self.bernM1.setObjectName("bernM1")
        self.verticalLayout_3.addWidget(self.bernM1)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_10 = QtWidgets.QLabel(Dialog)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_4.addWidget(self.label_10)
        self.bernM2 = QtWidgets.QSpinBox(Dialog)
        self.bernM2.setObjectName("bernM2")
        self.verticalLayout_4.addWidget(self.bernM2)
        self.horizontalLayout_2.addLayout(self.verticalLayout_4)
        self.layout_Bernuli.addLayout(self.horizontalLayout_2)
        self.verticalLayout_13.addLayout(self.layout_Bernuli)
        self.layout_poli = QtWidgets.QVBoxLayout()
        self.layout_poli.setObjectName("layout_poli")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_11 = QtWidgets.QLabel(Dialog)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_6.addWidget(self.label_11)
        self.poliN = QtWidgets.QSpinBox(Dialog)
        self.poliN.setObjectName("poliN")
        self.verticalLayout_6.addWidget(self.poliN)
        self.horizontalLayout_3.addLayout(self.verticalLayout_6)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.label_12 = QtWidgets.QLabel(Dialog)
        self.label_12.setObjectName("label_12")
        self.verticalLayout_7.addWidget(self.label_12)
        self.poliK = QtWidgets.QSpinBox(Dialog)
        self.poliK.setObjectName("poliK")
        self.verticalLayout_7.addWidget(self.poliK)
        self.horizontalLayout_3.addLayout(self.verticalLayout_7)
        self.layout_poli.addLayout(self.horizontalLayout_3)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.label_13 = QtWidgets.QLabel(Dialog)
        self.label_13.setObjectName("label_13")
        self.verticalLayout_8.addWidget(self.label_13)
        self.poliM = QtWidgets.QLineEdit(Dialog)
        self.poliM.setObjectName("poliM")
        self.verticalLayout_8.addWidget(self.poliM)
        self.layout_poli.addLayout(self.verticalLayout_8)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.label_14 = QtWidgets.QLabel(Dialog)
        self.label_14.setObjectName("label_14")
        self.verticalLayout_9.addWidget(self.label_14)
        self.poliP = QtWidgets.QLineEdit(Dialog)
        self.poliP.setObjectName("poliP")
        self.verticalLayout_9.addWidget(self.poliP)
        self.layout_poli.addLayout(self.verticalLayout_9)
        self.verticalLayout_13.addLayout(self.layout_poli)
        self.textResult = QtWidgets.QTextBrowser(Dialog)
        self.textResult.setObjectName("textResult")
        self.verticalLayout_13.addWidget(self.textResult)
        self.getResult = QtWidgets.QPushButton(Dialog)
        self.getResult.setAutoDefault(False)
        self.getResult.setObjectName("getResult")
        self.verticalLayout_13.addWidget(self.getResult)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Выберите форулу"))
        self.chooseFormula.setItemText(0, _translate("Dialog", "Формула Бернули"))
        self.chooseFormula.setItemText(1, _translate("Dialog", "Полиномиальная формула"))
        self.groupBern.setTitle(_translate("Dialog", "Выберите необходимую вероятность событий"))
        self.label_6.setText(_translate("Dialog", "p"))
        self.label_7.setText(_translate("Dialog", "n"))
        self.label_8.setText(_translate("Dialog", "m"))
        self.label_9.setText(_translate("Dialog", "m1"))
        self.label_10.setText(_translate("Dialog", "m2"))
        self.label_11.setText(_translate("Dialog", "n"))
        self.label_12.setText(_translate("Dialog", "k"))
        self.label_13.setText(_translate("Dialog", "m"))
        self.label_14.setText(_translate("Dialog", "p"))
        self.getResult.setText(_translate("Dialog", "Получить результат"))

