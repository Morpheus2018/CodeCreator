from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        layout = QGridLayout()
        self.setLayout(layout)

        radiobutton = QRadioButton("Australia")
        radiobutton.setChecked(True)
        radiobutton.country = "Australia"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 0)

        radiobutton = QRadioButton("China")
        radiobutton.country = "China"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 1)

        radiobutton = QRadioButton("Japan")
        radiobutton.country = "Japan"
        radiobutton.toggled.connect(self.onClicked)
        layout.addWidget(radiobutton, 0, 2)

    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            output = f'TESSSSSSSS\n '
            with open(FILENAME, "a", encoding='UTF-8') as output_file:
                output_file.write(output)
            print("Country is")

FILENAME = "output1.txt"

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())