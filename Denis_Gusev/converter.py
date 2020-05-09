#!/usr/bin/python3

import sys
import requests
import lxml.etree as ET
from datetime import date
from PyQt5.QtWidgets import QWidget, QApplication, QComboBox, QPushButton, QLabel, QLineEdit
from PyQt5.QtGui import QPixmap, QFont

class CBR_API(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
    
    def initUI(self):
        self.setFixedSize(300, 400)
        self.setWindowTitle("Currency Converter")

        self.source()
        self.target()

        convert_button = QPushButton("Convert", self)
        convert_button.move(200, 200)

        convert_button.clicked.connect(self.make_request)

        self.textbox = QLineEdit(self)
        self.textbox.move(25, 150)
        self.textbox.setFixedSize(100, 25)

        self.load_result_image()

        self.show()

    def source(self):
        self.source_combo = QComboBox(self)

        self.source_combo.addItem("USD")
        self.source_combo.addItem("RUB")
        self.source_combo.addItem("EUR")

        self.source_combo.move(50, 201)

    def target(self):
        self.target_combo = QComboBox(self)

        self.target_combo.addItem("RUB")
        self.target_combo.addItem("EUR")
        self.target_combo.addItem("USD")

        self.target_combo.move(125, 201)

    def make_request(self):
        source_text = self.source_combo.currentText()
        target_text = self.target_combo.currentText()

        today = date.today()
        year = today.year
        month = today.month
        day = today.day

        source_val = 1
        target_val = 1
        result = self.get_result(day, month, year)

        if source_text == "RUB":
            source_val = 1
        if source_text == "USD":
            source_val = result['dollar']
        if source_text == "EUR":
            source_val = result['euro']
        if target_text == "RUB":
            target_val = 1
        if target_text == "USD":
            target_val = result['dollar']
        if target_text == "EUR":
            target_val = result['euro']
        if (self.textbox.text() == ""):
            target_val = round(float(source_val)/float(target_val), 4)
            source_val = 1
        else:
            target_val = round(float(source_val)/float(target_val)*float(self.textbox.text()), 4)
            source_val = float(self.textbox.text())
        
        self.source_value.setText(f"{source_val} {source_text}")
        self.source_value.adjustSize()
        self.target_value.setText(f"{target_val} {target_text}")
        self.target_value.adjustSize()

    def get_result(self, day, month, year):

        result = {
            'dollar': 0,
            'euro': 0,
        }

        if (int(day)) < 10:
            day = f"0{day}"

        if (int(month)) < 10:
            month = f"0{month}"

        try:
            get_xml = requests.get(f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={day}/{month}/{year}')

            structure = ET.fromstring(get_xml.content)

        except:
            return result

        try:
            dollar = structure.find("./*[@ID='R01235']/Value")
            result['dollar'] = dollar.text.replace(',', '.')
        except:
            result['dollar'] = 'x'

        try:
            euro = structure.find("./*[@ID='R01239']/Value")
            result['euro'] = euro.text.replace(',', '.')
        except:
            result['euro'] = 'x'

        return result

    def load_result_image(self):
        self.source_value = QLabel('1 RUB', self)
        self.source_value.move(60, 100)

        self.middle_text = QLabel("is", self)
        self.middle_text.move(140, 100)

        self.target_value = QLabel('1 RUB', self)
        self.target_value.move(200, 100)

def main():
    app = QApplication(sys.argv)
    money = CBR_API()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
