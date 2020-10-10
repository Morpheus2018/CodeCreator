#!/usr/bin/env python3
# _*_ coding: utf-8 _*_

import sys
import PyQt5.uic as uic
import PyQt5.QtWidgets as widgets

app = widgets.QApplication(sys.argv)
w = uic.loadUi("qt5designer.v2.0.0.ui")


def clickmethod():
    output = f'<li><a href="{w.lineEditLINK.text()}" target="_blank"><img data-src="{w.lineEditBILD.text()}" class="lazyload" loading="lazy" title="{w.lineEditTITLE.text()}" border="2"/>{w.lineEditNAME.text()}</a></li>\n '
    with open(FILENAME, "a", encoding='UTF-8') as output_file:
        output_file.write(output)
    print(f'{output}')
    w.lineEditLINK.clear()
    w.lineEditBILD.clear()
    w.lineEditTITLE.clear()
    w.lineEditNAME.clear()

def onClicked(self):
    if w.radioButton_1.isChecked():
        file = open("output.txt", "a")
        file.write("Code für :" + w.radioButton_1.text() + "\n")
        file.close()
        w.groupBoxCode.setTitle("Code für " + w.radioButton_1.text())
        print("Code für :" + w.radioButton_1.text() + "\n")

def onClicked1(self):
    if w.radioButton_2.isChecked():
        file = open("output.txt", "a")
        file.write("Code für :" + w.radioButton_2.text() + "\n")
        file.close()
        w.groupBoxCode.setTitle("Code für " + w.radioButton_1.text())
        print("Code für :" + w.radioButton_2.text() + "\n")

def onClicked2(self):
    if w.radioButton_3.isChecked():
        file = open("output.txt", "a")
        file.write("Code für :" + w.radioButton_3.text() + "\n")
        file.close()
        w.groupBoxCode.setTitle("Code für " + w.radioButton_3.text())
        print("Code für :" + w.radioButton_3.text() + "\n")

def onClicked3(self):
    if w.radioButton_4.isChecked():
        file = open("output.txt", "a")
        file.write("Code für :" + w.radioButton_4.text() + "\n")
        file.close()
        w.groupBoxCode.setTitle("Code für " + w.radioButton_4.text())
        print("Code für :" + w.radioButton_4.text() + "\n")

FILENAME = "output.txt"

w.pushButtonSave.clicked.connect(clickmethod)
w.radioButton_1.toggled.connect(onClicked)
w.radioButton_2.toggled.connect(onClicked1)
w.radioButton_3.toggled.connect(onClicked2)
w.radioButton_4.toggled.connect(onClicked3)

w.show()
sys.exit(app.exec_())
