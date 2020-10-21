import sys
import subprocess
#import os #Für Windows
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi

OUTPUT_FILENAME = "output.txt"


class CodeCreator(QDialog):
    def __init__(self):
        super(CodeCreator, self).__init__()
        loadUi('qt5designer.v2.0.5.ui', self)
        self.pushButtonNext.clicked.connect(self.clickNext)
        self.pushButtonSave.clicked.connect(self.clickOffnen)
        self.radiobuttons = [
            self.radioButton1, self.radioButton2, self.radioButton3, self.radioButton4
        ]
        for radiobutton in self.radiobuttons:
            radiobutton.clicked.connect(self.checkRadioButtonState)

    def clickNext(self):
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

    def clickOffnen(self):
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, OUTPUT_FILENAME])
        #os.system(OUTPUT_FILENAME) #Für Windows

    def checkRadioButtonState(self):
        for radiobutton in self.radiobuttons:
            if radiobutton.isChecked():
                with open(OUTPUT_FILENAME, "a") as output:
                    text = radiobutton.text()
                    output.write(f"Code für: {text}\n")
                    self.groupBoxCode.setTitle("Code für: " + text)


def main():
    app = QApplication(sys.argv)
    cc = CodeCreator()
    cc.show()
    app.exec_()


if __name__ == '__main__':
    main()
