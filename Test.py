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

        radiobutton2 = QRadioButton("USA")
        radiobutton2.country = "USA"
        radiobutton2.toggled.connect(self.onClicked2)
        layout.addWidget(radiobutton2, 0, 3)

        radiobutton1 = QRadioButton("Japan")
        radiobutton1.country = "Japan"
        radiobutton1.toggled.connect(self.onClicked1)
        layout.addWidget(radiobutton1, 0, 2)

    def onClicked1, onClicked2(self):
        radioButton1 = self.sender()
        if radioButton1.isChecked():
            output = f'JAPANNNNNNNNNNN\n'
            with open(FILENAME1, "a", encoding='UTF-8') as output_file:
                output_file.write(output)
            print("Country is %s" % (radioButton1.country), (f'{output}'))



    def onClicked(self):
        radioButton = self.sender()
        if radioButton.isChecked():
            print("Country is %s" % (radioButton.country))

FILENAME1 = "output1.txt"
FILENAME2 = "output2.txt"

app = QApplication(sys.argv)
screen = Window()
screen.show()
sys.exit(app.exec_())