import sys

from collections import namedtuple
from PyQt5.QtWidgets import *


res = [0,0]
sign = ''
text = ''
label = ''

def writing1():
    global res, text, label
    res[0] = res[0]*10 + 1
    text = text + '1'
    label.setText(text)

def writing2():
    global res, text, label
    res[0] = res[0]*10 + 2
    text = text + '2'
    label.setText(text)

def writing3():
    global res, text, label
    res[0] =  res[0]*10 + 3
    text = text + '3'
    label.setText(text)

def writing4():
    global res, text, label
    res[0] =  res[0]*10 + 4
    text = text + '4'
    label.setText(text)

def writing5():
    global res, text, label
    res[0] = res[0]*10 + 5
    text = text + '5'
    label.setText(text)

def writing6():
    global res, text, label
    res[0] = res[0]*10 + 6
    text = text + '6'
    label.setText(text)

def writing7():
    global res, text, label
    res[0] =  res[0]*10 + 7
    text = text + '7'
    label.setText(text)

def writing8():
    global res, text, label
    res[0] =  res[0]*10 + 8
    text = text + '8'
    label.setText(text)

def writing9():
    global res, text, label
    res[0] =  res[0]*10 + 9
    text = text + '9'
    label.setText(text)

def writing0():
    global res, text, label
    res[0] =  res[0]*10
    text = text + '0'
    label.setText(text)

def calcSum():
    global sign, res, text, label
    sign = '+'
    res[1] = res[0]
    res[0] = 0
    text = text + sign
    label.setText(text)

def calcSub():
    global sign, res, text, label
    sign = '-'
    res[1] = res[0]
    res[0] = 0
    text = text + sign
    label.setText(text)

def calcMul():
    global sign, res, text, label
    sign = '*'
    res[1] = res[0]
    res[0] = 0
    text = text + sign
    label.setText(text)

def calcDiv():
    global sign, res, text, label
    sign = '/'
    res[1] = res[0]
    res[0] = 0
    text = text + sign
    label.setText(text)

def calcDel():
    global sign, res, text, label
    sign = ''
    res[1] , res[0] = 0, 0
    text = ''
    label.setText(text)

def equal():
    global sign, res, text, label
    if (sign == '+'):
        res[1] = res[1] + res[0]
    elif(sign == '-'):
        res[1] = res[1] - res[0]
    elif(sign == '*'):
        res[1] = res[1] * res[0]
    elif(sign == '/'):
        if (res[0] == 0):
            text = 'Error'
        else:
            res[1] = res[1] / res[0]
    if text != "Error":
        text = f'{res[1]}'
    res = [0,0]
    label.setText(text)
    

def main():
    global sign, res, text, label
    app = QApplication([])
    w = QWidget()
    w.setWindowTitle('Calculator')

    grid = QGridLayout(w)

    label = QLabel(text)
    grid.addWidget(label, 0, 0, 1, 0)

    btns = [QPushButton(f'{i}') for i in range(10)]
    for i in range (3):
        for j in range(3):
            grid.addWidget(btns[i*3 + j + 1], i+1, j)

    btnEq = QPushButton('=')
    btnSum = QPushButton('+')
    btnSub = QPushButton('-')
    btnMul = QPushButton('*')
    btnDiv = QPushButton('/')
    btnDel = QPushButton('Del')


    grid.addWidget(btnSum,  1, 3)
    grid.addWidget(btnSub,  2, 3)
    grid.addWidget(btnMul,  3, 3)
    grid.addWidget(btnDel,  4, 0)
    grid.addWidget(btns[0], 4, 1)
    grid.addWidget(btnEq,   4, 2)
    grid.addWidget(btnDiv,  4, 3)

    btns[1].clicked.connect(writing1) # widget.signal.connect(slot)
    btns[2].clicked.connect(writing2) 
    btns[3].clicked.connect(writing3) 
    btns[4].clicked.connect(writing4) 
    btns[5].clicked.connect(writing5) 
    btns[6].clicked.connect(writing6) 
    btns[7].clicked.connect(writing7) 
    btns[8].clicked.connect(writing8) 
    btns[9].clicked.connect(writing9) 
    btns[0].clicked.connect(writing0) 
    
    btnEq.clicked.connect(equal) 
    btnSum.clicked.connect(calcSum) 
    btnSub.clicked.connect(calcSub) 
    btnMul.clicked.connect(calcMul) 
    btnDiv.clicked.connect(calcDiv) 
    btnDel.clicked.connect(calcDel) 


    w.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
