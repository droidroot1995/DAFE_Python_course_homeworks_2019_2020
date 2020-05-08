import sys
import requests
import lxml.etree as ET
from datetime import datetime as dt
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QPalette


class Converter(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):

        self.result = QLabel(self)

        self.digit1 = QLineEdit(self)
        self.digit1.setText('0')

        self.op1 = QComboBox(self)
        self.op1.addItems(['RUB', 'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 
                           'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 
                           'KZT', 'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 
                           'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 
                           'UAH', 'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY'])

        self.digit2 = QLineEdit(self)
        self.digit2.setText('0')

        self.op2 = QComboBox(self)
        self.op2.addItems(['RUB', 'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 
                           'BRL', 'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 
                           'KZT', 'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 
                           'RON', 'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 
                           'UAH', 'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY'])

        self.btn = QPushButton(self)
        self.btn.setText('Сконвертировать')
        self.btn.clicked.connect(self.calculate)

        self.hbox = QHBoxLayout(self)
        for i in [self.digit1, self.op1, self.digit2, self.op2, self.btn]:
            self.hbox.addWidget(i)


        self.resize(500, 300)
        self.setWindowTitle('Конвертер валют')
        self.show()



    def get_curs(self, text):
        now = dt.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day)

        if len(day) < 2:
            day = '0' + day

        if len(month) < 2:
            month = '0' + month

        try:
            get_xml = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}')


            structure = ET.fromstring(get_xml.content)
        except:
            return 'ERROR1'

        indexes = {'AUD' : '010',
                'AZN' : '020A',
                'GBP' : '035',
                'AMD' : '060',
                'BYN' : '090B',
                'BGN' : '100',
                'BRL' : '115',
                'HUF' : '135',
                'HKD' : '200',
                'DKK' : '215',
                'USD' : '235',
                'EUR' : '239', 
                'INR' : '270', 
                'KZT' : '335',
                'CAD' : '350', 
                'KGS' : '370', 
                'CNY' : '375', 
                'MDL' : '500', 
                'NOK' : '535', 
                'PLN' : '565', 
                'RON' : '585F',
                'XDR' : '589', 
                'SGD' : '625', 
                'TJS' : '670', 
                'TRY' : '700J', 
                'TMT' : '710A', 
                'UZS' : '717', 
                'UAH' : '720',
                'CZK' : '760', 
                'SEK' : '770', 
                'CHF' : '775', 
                'ZAR' : '810', 
                'KRW' : '815', 
                'JPY' : '820'}

        index = 'R01' + indexes[text]
    

        try:
            current = structure.find(f"./*[@ID='{index}']/Value").text.replace(',', '.')
            return current
        except:
            return ERROR2


    def calculate(self):
        try:
            
            d1 = float(self.digit1.text())

            val1 = self.op1.currentText()

            d2 = float(self.digit2.text())

            val2 = self.op2.currentText()

            curs1 = '1'

            curs2 = '1'

            if val1 != 'RUB':
                curs1 = self.get_curs(val1)

            if val2 != 'RUB':
                curs2 = self.get_curs(val2)
            
            if d1 == 0.0:
                tmp = d2 * (float(curs2) / float(curs1))
                tmp = round(tmp, 2)
                self.digit1.setText(str(tmp))
            
            else:
                tmp = d1 * (float(curs1) / float(curs2))
                tmp = round(tmp, 2)
            self.digit2.setText(str(tmp))


        except:
            self.digit1.setText('ERROR')
            self.digit2.setText('ERROR')

    

def main():
    app = QApplication(sys.argv)
    calc = Converter()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
