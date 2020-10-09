# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.14.1


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QDialog, QRadioButton, QHBoxLayout, QGroupBox, QVBoxLayout, QLabel

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(875, 273)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        #radioButton_1
        self.radioButton_1 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_1.setChecked(True)
        self.radioButton_1.setObjectName("radioButton_1")
        self.radioButton_1.toggled.connect(self.onClicked)
        self.horizontalLayout.addWidget(self.radioButton_1)
        #radioButton_2
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.toggled.connect(self.onClicked)
        self.horizontalLayout.addWidget(self.radioButton_2)
        # radioButton_4
        self.radioButton_3 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_3.toggled.connect(self.onClicked)
        #radioButton_4
        self.radioButton_4 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout.addWidget(self.radioButton_4)
        self.radioButton_4.toggled.connect(self.onClicked)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBoxCode = QtWidgets.QGroupBox(Dialog)
        self.groupBoxCode.setObjectName("groupBoxCode")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCode)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditLINK = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditLINK.setObjectName("lineEditLINK")
        self.gridLayout.addWidget(self.lineEditLINK, 1, 1, 1, 1)
        self.labelLINK = QtWidgets.QLabel(self.groupBoxCode)
        self.labelLINK.setObjectName("labelLINK")
        self.gridLayout.addWidget(self.labelLINK, 1, 0, 1, 1)
        self.labelBILD = QtWidgets.QLabel(self.groupBoxCode)
        self.labelBILD.setObjectName("labelBILD")
        self.gridLayout.addWidget(self.labelBILD, 2, 0, 1, 1)
        self.lineEditNAME = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditNAME.setObjectName("lineEditNAME")
        self.gridLayout.addWidget(self.lineEditNAME, 4, 1, 1, 1)
        self.labelTITLE = QtWidgets.QLabel(self.groupBoxCode)
        self.labelTITLE.setObjectName("labelTITLE")
        self.gridLayout.addWidget(self.labelTITLE, 3, 0, 1, 1)
        self.lineEditTITLE = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditTITLE.setObjectName("lineEditTITLE")
        self.gridLayout.addWidget(self.lineEditTITLE, 3, 1, 1, 1)
        self.labelNAME = QtWidgets.QLabel(self.groupBoxCode)
        self.labelNAME.setObjectName("labelNAME")
        self.gridLayout.addWidget(self.labelNAME, 4, 0, 1, 1)
        self.lineEditBILD = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditBILD.setObjectName("lineEditBILD")
        self.gridLayout.addWidget(self.lineEditBILD, 2, 1, 1, 1)
        self.splitter = QtWidgets.QSplitter(self.groupBoxCode)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonSave = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonSave.setObjectName("pushButtonSave")
        self.horizontalLayout_2.addWidget(self.pushButtonSave)
        self.pushButtonEde = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonEde.setObjectName("pushButtonEde")
        self.horizontalLayout_2.addWidget(self.pushButtonEde)
        self.gridLayout.addWidget(self.splitter, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxCode)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Dialog)
        self.pushButtonEde.clicked.connect(Dialog.close)
        self.pushButtonSave.clicked.connect(self.clickMethod)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.lineEditLINK, self.lineEditBILD)
        Dialog.setTabOrder(self.lineEditBILD, self.lineEditTITLE)
        Dialog.setTabOrder(self.lineEditTITLE, self.lineEditNAME)
        Dialog.setTabOrder(self.lineEditNAME, self.pushButtonSave)
        Dialog.setTabOrder(self.pushButtonSave, self.pushButtonEde)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "CodeCreator  v2.0.0"))
        self.radioButton_1.setToolTip(_translate("dialog", "Standard-Aktiviert"))
        self.radioButton_1.setText(_translate("dialog", "Code-1"))
        self.radioButton_2.setText(_translate("dialog", "Code-2"))
        self.radioButton_3.setText(_translate("dialog", "Code-3"))
        self.radioButton_4.setText(_translate("dialog", "Code-3"))
        self.groupBoxCode.setTitle(_translate("dialog", "Code"))
        self.lineEditLINK.setPlaceholderText(_translate("dialog", "https://LINK.com"))
        self.labelLINK.setText(_translate("dialog", "LINK"))
        self.labelBILD.setText(_translate("dialog", "BILD"))
        self.lineEditNAME.setPlaceholderText(_translate("dialog", "Name"))
        self.labelTITLE.setText(_translate("dialog", "TITLE"))
        self.lineEditTITLE.setPlaceholderText(_translate("dialog", "Titel"))
        self.labelNAME.setText(_translate("dialog", "NAME"))
        self.lineEditBILD.setPlaceholderText(_translate("dialog", "https://BILD.jpg"))
        self.pushButtonSave.setText(_translate("dialog", "Speichern"))
        self.pushButtonEde.setText(_translate("dialog", "Beenden"))

    def clickMethod(self):
            output = f'<li><a href="{self.lineEditLINK.text()}" target="_blank"><img data-src="{self.lineEditBILD.text()}" class="lazyload" loading="lazy" title="{self.lineEditTITLE.text()}" border="2"/>{self.lineEditNAME.text()}</a></li>\n '
            with open(FILENAME1, "a", encoding='UTF-8') as output_file:
                output_file.write(output)
            print(f'{output}')
            (self.lineEditLINK.clear())
            (self.lineEditBILD.clear())
            (self.lineEditTITLE.clear())
            (self.lineEditNAME.clear())

    def onClicked(self):
        radioButt = self.sender()
        if self.radioButt.isChecked():
            file = open("output1.txt", "a")
            file.write("You Have Selected :" + self.radioButt.text() + "\n")
            file.close()
            self.groupBoxCode.setTitle("You Have Selected " + self.radioButt.text())
            print("You Have Selected :" + self.radioButt.text() + "\n")


FILENAME = "output.txt"
FILENAME1 = "output1.txt"


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
