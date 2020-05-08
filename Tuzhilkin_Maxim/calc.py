import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QPalette


class Calculator(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
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



    def calculate(self):
        try:
            
            d1 = float(self.digit1.text())

            opp = self.op.currentText()

            d2 = float(self.digit2.text())
            
            do = {'+' : d1 + d2,
                  '-' : d1 - d2,
                  '*' : d1 * d2,
                  '%' : d1 % d2,
                  '^' : d1 ** d2,
                  '/' : d1 / d2}
            x = do[opp]
            
        except:
            x = 'error'

        self.result.setText(str(x))

    

def main():
    app = QApplication(sys.argv)
    calc = Calculator()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
