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


FILENAME = "output.txt"

w.pushButtonSave.clicked.connect(clickmethod)
#w.radioButton_1.clicked.toggled.connect(onClicked)

w.show()
sys.exit(app.exec_())
