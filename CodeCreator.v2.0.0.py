# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.14.1


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(643, 299)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.radioButton1 = QtWidgets.QRadioButton(dialog)
        self.radioButton1.setChecked(True)
        self.radioButton1.setObjectName("radioButton1")
        self.horizontalLayout.addWidget(self.radioButton1)
        self.radioButton2 = QtWidgets.QRadioButton(dialog)
        self.radioButton2.setObjectName("radioButton2")
        self.horizontalLayout.addWidget(self.radioButton2)
        self.radioButton3 = QtWidgets.QRadioButton(dialog)
        self.radioButton3.setObjectName("radioButton3")
        self.horizontalLayout.addWidget(self.radioButton3)
        self.radioButton4 = QtWidgets.QRadioButton(dialog)
        self.radioButton4.setObjectName("radioButton4")
        self.horizontalLayout.addWidget(self.radioButton4)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.groupBoxCode = QtWidgets.QGroupBox(dialog)
        self.groupBoxCode.setObjectName("groupBoxCode")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCode)
        self.gridLayout.setObjectName("gridLayout")
        self.labelLINK = QtWidgets.QLabel(self.groupBoxCode)
        self.labelLINK.setObjectName("labelLINK")
        self.gridLayout.addWidget(self.labelLINK, 1, 0, 1, 1)
        self.labelTITLE = QtWidgets.QLabel(self.groupBoxCode)
        self.labelTITLE.setObjectName("labelTITLE")
        self.gridLayout.addWidget(self.labelTITLE, 3, 0, 1, 1)
        self.labelNAME = QtWidgets.QLabel(self.groupBoxCode)
        self.labelNAME.setObjectName("labelNAME")
        self.gridLayout.addWidget(self.labelNAME, 4, 0, 1, 1)
        self.lineEditNAME = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditNAME.setObjectName("lineEditNAME")
        self.gridLayout.addWidget(self.lineEditNAME, 4, 1, 1, 1)
        self.lineEditBILD = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditBILD.setObjectName("lineEditBILD")
        self.gridLayout.addWidget(self.lineEditBILD, 2, 1, 1, 1)
        self.lineEditLINK = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditLINK.setObjectName("lineEditLINK")
        self.gridLayout.addWidget(self.lineEditLINK, 1, 1, 1, 1)
        self.labelBILD = QtWidgets.QLabel(self.groupBoxCode)
        self.labelBILD.setObjectName("labelBILD")
        self.gridLayout.addWidget(self.labelBILD, 2, 0, 1, 1)
        self.lineEditTITLE = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditTITLE.setObjectName("lineEditTITLE")
        self.gridLayout.addWidget(self.lineEditTITLE, 3, 1, 1, 1)
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
        self.gridLayout.addWidget(self.splitter, 6, 1, 1, 1)
        self.labelInfo = QtWidgets.QLabel(self.groupBoxCode)
        self.labelInfo.setText("")
        self.labelInfo.setObjectName("labelInfo")
        self.gridLayout.addWidget(self.labelInfo, 5, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBoxCode)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(dialog)
        self.pushButtonEde.clicked.connect(dialog.close)
        self.pushButtonSave.clicked.connect(self.clickSave)
        self.radiobuttons = [
            self.radioButton1, self.radioButton2, self.radioButton3, self.radioButton4
        ]
        for radiobutton in self.radiobuttons:
            radiobutton.clicked.connect(self.checkRadioButtonState)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.lineEditLINK, self.lineEditBILD)
        dialog.setTabOrder(self.lineEditBILD, self.lineEditTITLE)
        dialog.setTabOrder(self.lineEditTITLE, self.lineEditNAME)
        dialog.setTabOrder(self.lineEditNAME, self.radioButton1)
        dialog.setTabOrder(self.radioButton1, self.pushButtonSave)
        dialog.setTabOrder(self.pushButtonSave, self.pushButtonEde)
        dialog.setTabOrder(self.pushButtonEde, self.radioButton2)
        dialog.setTabOrder(self.radioButton2, self.radioButton3)
        dialog.setTabOrder(self.radioButton3, self.radioButton4)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "CodeCreator  v2.0.0"))
        self.radioButton1.setToolTip(_translate("dialog", "Standard-Seite1"))
        self.radioButton1.setText(_translate("dialog", "Seite 1"))
        self.radioButton2.setText(_translate("dialog", "Seite 2"))
        self.radioButton3.setText(_translate("dialog", "Seite 3"))
        self.radioButton4.setText(_translate("dialog", "Seite 4"))
        self.groupBoxCode.setTitle(_translate("dialog", "Code für: Seite 1"))
        self.labelLINK.setText(_translate("dialog", "LINK"))
        self.labelTITLE.setText(_translate("dialog", "TITLE"))
        self.labelNAME.setText(_translate("dialog", "NAME"))
        self.lineEditNAME.setPlaceholderText(_translate("dialog", "Name"))
        self.lineEditBILD.setPlaceholderText(_translate("dialog", "https://BILD.jpg"))
        self.lineEditLINK.setPlaceholderText(_translate("dialog", "https://LINK.com"))
        self.labelBILD.setText(_translate("dialog", "BILD"))
        self.lineEditTITLE.setPlaceholderText(_translate("dialog", "Titel"))
        self.pushButtonSave.setText(_translate("dialog", "Speichern"))
        self.pushButtonEde.setText(_translate("dialog", "Beenden"))

    def clickSave(self):
        output = f'<li><a href="{self.lineEditLINK.text()}" target="_blank"><img data-src="{self.lineEditBILD.text()}" class="lazyload" loading="lazy" title="{self.lineEditTITLE.text()}" border="2"/>{self.lineEditNAME.text()}</a></li>\n '
        with open(OUTPUT_FILENAME, "a", encoding='UTF-8') as output_file:
            output_file.write(output)
        print(f'{output}')
        info = self.lineEditTITLE.text() + "  Hinzugefügt"
        self.labelInfo.setText(info)
        self.lineEditLINK.clear()
        self.lineEditBILD.clear()
        self.lineEditTITLE.clear()
        self.lineEditNAME.clear()

    def checkRadioButtonState(self):
        for radiobutton in self.radiobuttons:
            if radiobutton.isChecked():
                with open(OUTPUT_FILENAME, "a") as output:
                    text = radiobutton.text()
                    output.write(f"Code für: {text}\n")
                    self.groupBoxCode.setTitle("Code für: " + text)


OUTPUT_FILENAME = "output.txt"


def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
