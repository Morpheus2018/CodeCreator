# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mytest.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(448, 148)
        Dialog.setWindowTitle("Radio Button")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(Dialog)
        self.groupBox.setTitle("What Is Your Favorite Programming Language ?")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radiobtn1 = QtWidgets.QRadioButton(self.groupBox)
        self.radiobtn1.setText("Football")
        self.radiobtn1.setChecked(True)
        self.radiobtn1.setObjectName("radiobtn1")
        self.horizontalLayout.addWidget(self.radiobtn1)
        self.radiobtn1.toggled.connect(self.onRadioBtn)
        self.radiobtn2 = QtWidgets.QRadioButton(self.groupBox)
        self.radiobtn2.setText("Cricket")
        self.radiobtn2.setObjectName("radiobtn2")
        self.horizontalLayout.addWidget(self.radiobtn2)
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        #self.radiobtn2.toggled.connect(self.onRadioBtn1)
        self.radiobtn3 = QtWidgets.QRadioButton(self.groupBox)
        self.radiobtn3.setText("Tennis")
        self.radiobtn3.setObjectName("radiobtn3")
        self.horizontalLayout.addWidget(self.radiobtn3)
        self.radiobtn2.toggled.connect(self.onRadioBtn)
        #self.radiobtn3.toggled.connect(self.onRadioBtn2)
        self.verticalLayout.addWidget(self.groupBox)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        pass

    def onRadioBtn(self):
        radioBtn = self.sender()
        if radioBtn.isChecked():
            self.label.setText("You Have Selected " + radioBtn.text())

#    def onRadioBtn(self):
#        if self.radiobtn1.isChecked():
#           self.label.setText("You Have Selected " + self.radiobtn1.text())

#    def onRadioBtn1(self):
#        if self.radiobtn2.isChecked():
#            self.label.setText("You Have Selected " + self.radiobtn2.text())

#    def onRadioBtn2(self):
#        if self.radiobtn3.isChecked():
#            self.label.setText("You Have Selected " + self.radiobtn3.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
