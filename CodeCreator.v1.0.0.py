#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Created by: PyQt5 UI code generator 5.14.1

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_dialog(object):
    def setupUi(self, dialog):
        dialog.setObjectName("dialog")
        dialog.resize(666, 231)
        self.horizontalLayout = QtWidgets.QHBoxLayout(dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBoxCode = QtWidgets.QGroupBox(dialog)
        self.groupBoxCode.setObjectName("groupBoxCode")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBoxCode)
        self.gridLayout.setObjectName("gridLayout")
        self.lineEditBILD = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditBILD.setObjectName("lineEditBILD")
        self.gridLayout.addWidget(self.lineEditBILD, 2, 1, 1, 1)
        self.labelNAME = QtWidgets.QLabel(self.groupBoxCode)
        self.labelNAME.setObjectName("labelNAME")
        self.gridLayout.addWidget(self.labelNAME, 4, 0, 1, 1)
        self.labelLINK = QtWidgets.QLabel(self.groupBoxCode)
        self.labelLINK.setObjectName("labelLINK")
        self.gridLayout.addWidget(self.labelLINK, 1, 0, 1, 1)
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
        self.labelBILD = QtWidgets.QLabel(self.groupBoxCode)
        self.labelBILD.setObjectName("labelBILD")
        self.gridLayout.addWidget(self.labelBILD, 2, 0, 1, 1)
        self.lineEditLINK = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditLINK.setObjectName("lineEditLINK")
        self.gridLayout.addWidget(self.lineEditLINK, 1, 1, 1, 1)
        self.lineEditNAME = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditNAME.setObjectName("lineEditNAME")
        self.gridLayout.addWidget(self.lineEditNAME, 4, 1, 1, 1)
        self.lineEditTITLE = QtWidgets.QLineEdit(self.groupBoxCode)
        self.lineEditTITLE.setObjectName("lineEditTITLE")
        self.gridLayout.addWidget(self.lineEditTITLE, 3, 1, 1, 1)
        self.labelTITLE = QtWidgets.QLabel(self.groupBoxCode)
        self.labelTITLE.setObjectName("labelTITLE")
        self.gridLayout.addWidget(self.labelTITLE, 3, 0, 1, 1)
        self.horizontalLayout.addWidget(self.groupBoxCode)

        self.retranslateUi(dialog)
        self.pushButtonEde.clicked.connect(dialog.close)
        self.pushButtonSave.clicked.connect(self.clickMethod)
        QtCore.QMetaObject.connectSlotsByName(dialog)
        dialog.setTabOrder(self.lineEditLINK, self.lineEditBILD)
        dialog.setTabOrder(self.lineEditBILD, self.lineEditTITLE)
        dialog.setTabOrder(self.lineEditTITLE, self.lineEditNAME)
        dialog.setTabOrder(self.lineEditNAME, self.pushButtonSave)
        dialog.setTabOrder(self.pushButtonSave, self.pushButtonEde)

    def retranslateUi(self, dialog):
        _translate = QtCore.QCoreApplication.translate
        dialog.setWindowTitle(_translate("dialog", "CodeCreator  v1.0.0"))
        self.groupBoxCode.setTitle(_translate("dialog", "Code"))
        self.lineEditBILD.setPlaceholderText(_translate("dialog", "https://BILD.jpg"))
        self.labelNAME.setText(_translate("dialog", "NAME"))
        self.labelLINK.setText(_translate("dialog", "LINK"))
        self.pushButtonSave.setText(_translate("dialog", "Speichern"))
        self.pushButtonEde.setText(_translate("dialog", "Beenden"))
        self.labelBILD.setText(_translate("dialog", "BILD"))
        self.lineEditLINK.setPlaceholderText(_translate("dialog", "https://LINK.com"))
        self.lineEditNAME.setPlaceholderText(_translate("dialog", "Name"))
        self.lineEditTITLE.setPlaceholderText(_translate("dialog", "Titel"))
        self.labelTITLE.setText(_translate("dialog", "TITLE"))


    def clickMethod(self):
        output = f'<li><a href="{self.lineEditLINK.text()}" target="_blank"><img data-src="{self.lineEditBILD.text()}" class="lazyload" loading="lazy" title="{self.lineEditTITLE.text()}" border="2"/>{self.lineEditNAME.text()}</a></li>\n '
        with open(FILENAME, "a", encoding='UTF-8') as output_file:
            output_file.write(output)
        print(f'{output}'), (self.lineEditLINK.clear()), (self.lineEditBILD.clear()), (self.lineEditTITLE.clear()), (self.lineEditNAME.clear())


FILENAME = "output.txt"
    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    dialog = QtWidgets.QDialog()
    ui = Ui_dialog()
    ui.setupUi(dialog)
    dialog.show()
    sys.exit(app.exec_())
