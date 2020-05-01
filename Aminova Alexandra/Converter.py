import sys
import requests # pip install requests
import lxml.etree as ET # pip install lxml
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QComboBox, QPushButton, QLineEdit)
from PyQt5.QtGui import QPixmap, QFont


class CBR_CONV(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        logo_label = QLabel(self)
        logo_label.setPixmap(QPixmap('img/exchange.png'))
        logo_label.move(75, 0)

        self.currency_from()
        self.amount()

        ok_button = QPushButton('OK', self)
        ok_button.resize(50, 23)
        ok_button.move(220, 198)

        ok_button.clicked.connect(self.make_request)

        self.load_result_image()

        self.setFixedSize(300, 400)
        self.setWindowTitle('Конвертер валют')
        self.show()

    def currency_from(self):
        self.currency_from_combo = QComboBox(self)

        currency_from_label = QLabel('Валюта:', self)
        currency_from_label.move(40, 170)

        self.currency_from_combo.addItem('USD')
        self.currency_from_combo.addItem('EUR')
        self.currency_from_combo.addItem('RUB')

        self.currency_from_combo.move(40, 200)

    def amount(self):
        self.amount_text = QLineEdit(self)
        self.amount_text.resize(110, 20)
        self.amount_text.move(100, 200)

        amount_label = QLabel('Сумма:', self)
        amount_label.move(127, 170)


    def make_request(self):
        currency_from_value = self.currency_from_combo.currentText()
        amount = self.amount_text.text()

        try:
            amount = int(amount)
        except ValueError:
            QMessageBox.warning(self, 'Внимание', 'Введено невалидное число: "{}"'.format(amount))
            amount = 0

        result = self.get_result(currency_from_value, amount)

        self.ruble_value.setText(f"{result['RUB']} руб")
        self.ruble_value.adjustSize()

        self.dollar_value.setText(f"{result['USD']} $")
        self.dollar_value.adjustSize()

        self.euro_value.setText(f"{result['EUR']} euro")
        self.euro_value.adjustSize()

    def get_result(self, currency_from, amount):
        
        result = {
            'RUB': 0,
            'USD': 0,
            'EUR': 0,
        }

        day = '21'
        month = '04'
        year = '2020'
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
            return result

        try:
            dollar = structure.find("./*[@ID='R01235']/Value")
            result['USD'] = dollar.text.replace(',', '.')
        except:
            result['USD'] = 'x'

        try:
            euro = structure.find("./*[@ID='R01239']/Value")
            result['EUR'] = euro.text.replace(',', '.')
        except:
            result['EUR'] = 'x'

        if currency_from == 'RUB':
            result['RUB'] = "%.2f" % amount
            result['USD'] = "%.2f" % (amount / float(result['USD']))
            result['EUR'] = "%.2f" % (amount / float(result['EUR']))

        elif currency_from == 'EUR':
            result['RUB'] = "%.2f" % (amount * float(result['EUR']))
            result['USD'] = "%.2f" % (float(result['RUB']) / float(result['USD']))
            result['EUR'] = "%.2f" % amount 

        elif currency_from == 'USD':
            result['RUB'] = "%.2f" % (amount * float(result['USD']))
            result['EUR'] = "%.2f" % (float(result['RUB']) / float(result['EUR']))
            result['USD'] = "%.2f" % amount 

        return result

    def load_result_image(self):

        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(18)

        ruble_label = QLabel(self)
        ruble_label.setPixmap(QPixmap('img/ruble.png'))
        ruble_label.resize(32, 32)
        ruble_label.move(30, 250)

        self.ruble_value = QLabel('0 руб', self)
        self.ruble_value.setFont(font)
        self.ruble_value.move(80, 250)

        dollar_label = QLabel(self)
        dollar_label.setPixmap(QPixmap('img/dollar.png'))
        dollar_label.move(30, 300)

        self.dollar_value = QLabel('0 руб', self)
        self.dollar_value.setFont(font)
        self.dollar_value.move(80, 300)

        euro_label = QLabel(self)
        euro_label.setPixmap(QPixmap('img/euro.png'))
        euro_label.move(30, 350)

        self.euro_value = QLabel('0 руб', self)
        self.euro_value.setFont(font)
        self.euro_value.move(80, 350)

def main():
    app = QApplication(sys.argv)
    money = CBR_CONV()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
