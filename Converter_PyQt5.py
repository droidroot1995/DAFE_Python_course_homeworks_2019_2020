#!/usr/bin/python3

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
        self.theme = QComboBox(self)
        self.theme.addItems(['Light', 'Dark'])
        self.theme.move(400, 0)

        self.btn2 = QPushButton(self)
        self.btn2.setText('Применить')
        self.btn2.move(400, 30)
        self.btn2.clicked.connect(self.Change_Theme)

        self.result = QLabel(self)

        self.digit1 = QLineEdit(self)
        self.digit1.setText('0')

        self.op1 = QComboBox(self)
        self.op1.addItems(['RUB', 'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL',
                          'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT',
                         'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON',
                        'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH',
                       'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY'])

        self.digit2 = QLineEdit(self)
        self.digit2.setText('0')

        self.op2 = QComboBox(self)
        self.op2.addItems(['RUB', 'AUD', 'AZN', 'GBP', 'AMD', 'BYN', 'BGN', 'BRL',
                          'HUF', 'HKD', 'DKK', 'USD', 'EUR', 'INR', 'KZT',
                         'CAD', 'KGS', 'CNY', 'MDL', 'NOK', 'PLN', 'RON',
                        'XDR', 'SGD', 'TJS', 'TRY', 'TMT', 'UZS', 'UAH',
                       'CZK', 'SEK', 'CHF', 'ZAR', 'KRW', 'JPY'])

        self.btn = QPushButton(self)
        self.btn.setText('Enter')
        self.btn.clicked.connect(self.calculate)

        self.hbox = QHBoxLayout(self)
        for i in [self.digit1, self.op1, self.digit2, self.op2, self.btn]:
            self.hbox.addWidget(i)


        self.resize(500, 300)
        self.setWindowTitle('Конвертер валют')
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
            # request: 'http://www.cbr.ru/scripts/XML_daily.asp?date_req=ДД/ММ/ГГГ'
            get_xml = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}')
            '''response: 
                <ValCurs Date="22.04.2017" name="Foreign Currency Market">
                <Valute ID="R01235">
                    <NumCode>840</NumCode>
                    <CharCode>USD</CharCode>
                    <Nominal>1</Nominal>
                    <Name>Доллар США</Name>
                    <Value>56,2307</Value>
                </Valute>
            
                <Valute ID="R01239">
                    <NumCode>978</NumCode>
                    <CharCode>EUR</CharCode>
                    <Nominal>1</Nominal>
                    <Name>Евро</Name>
                    <Value>60,3187</Value>
                </Valute>
            </ValCurs>'''

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

            opp1 = self.op1.currentText()

            d2 = float(self.digit2.text())

            opp2 = self.op2.currentText()

            curs1 = '1'

            curs2 = '1'

            if opp1 != 'RUB':
                curs1 = self.get_curs(opp1)

            if opp2 != 'RUB':
                curs2 = self.get_curs(opp2)
            
            if d1 == 0.0:
                tmp = d2 * (float(curs2) / float(curs1))

                if tmp > 10000: 
                    tmp = round(tmp, 0)
                elif tmp > 1:
                    tmp = round(tmp, 5)
                else: tmp = round(tmp, 11)

                self.digit1.setText(f'{str(tmp)}')
            
            else:
                tmp = d1 * (float(curs1) / float(curs2))

                if tmp > 10000: 
                    tmp = round(tmp, 0)
                elif tmp > 1:
                    tmp = round(tmp, 5)
                else: tmp = round(tmp, 11)

                self.digit2.setText(f'{str(tmp)}')


        except:
            self.digit1.setText('ERROR')
            self.digit2.setText('ERROR')

    

def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    calc = Converter()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

