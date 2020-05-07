#!/usr/bin/python3

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QPalette


class Calculater(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.theme = QComboBox(self)
        self.theme.addItems(['Light', 'Dark'])
        self.theme.move(200, 0)

        self.btn2 = QPushButton(self)
        self.btn2.setText('Применить')
        self.btn2.move(200, 30)
        self.btn2.clicked.connect(self.Change_Theme)

        self.result = QLabel(self)

        self.digit1 = QLineEdit(self)

        self.op = QComboBox(self)
        self.op.addItems(['+', '-', '*', '/', '%', '^'])

        self.digit2 = QLineEdit(self)

        self.btn = QPushButton(self)
        self.btn.setText('=')
        self.btn.clicked.connect(self.calculate)

        self.hbox = QHBoxLayout(self)
        for i in [self.digit1, self.op, self.digit2, self.btn, self.result]:
            self.hbox.addWidget(i)


        self.resize(300, 300)
        self.setWindowTitle('Калькулятор')
        self.show()

    def Change_Theme(self):
        th = self.theme.currentText()
        qp = QPalette()
        if th == 'Dark':
            qp.setColor(QPalette.WindowText, Qt.white)
            qp.setColor(QPalette.ButtonText, Qt.black)
            qp.setColor(QPalette.Button, Qt.white)
            qp.setColor(QPalette.Window, Qt.black)
        self.setPalette(qp)


    def calculate(self):
        try:
            
            d1 = float(self.digit1.text())

            opp = self.op.currentText()

            d2 = float(self.digit2.text())

            x = 0
            if opp == '+':
                x = d1 + d2
            elif opp == '-':
                x = d1 - d2
            elif opp == '*':
                x = d1 * d2
            elif opp == '%':
                x = d1 % d2
            elif opp == '^':
                x = d1 ** d2
            elif opp == '/':
                x = d1 / d2
        except:
            x = 'ERROR'

        self.result.setText(str(x))

    

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')



    calc = Calculater()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
