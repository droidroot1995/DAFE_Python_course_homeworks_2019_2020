import sys
import requests 
import lxml.etree as ET 
from PyQt5.QtWidgets import QApplication, QComboBox, QLabel, QLineEdit, QPushButton, QWidget
from PyQt5.QtGui import QPixmap, QFont


class CBR_API(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.days()
        self.month()
        self.year()
        self.from_value()
        self.from_cur()
        self.to_cur()

        ok_button = QPushButton('OK', self)
        ok_button.resize(50, 23)
        ok_button.move(220, 98)

        ok_button.clicked.connect(self.make_request)

        self.load_result_image()

        self.setFixedSize(300, 400)
        self.setWindowTitle('Currency converter for date')
        self.show()

    def days(self):
        self.days_combo = QComboBox(self)

        day_label = QLabel('day', self)
        day_label.move(20, 70)

        for day in range(1, 32):
            self.days_combo.addItem(f'{day}')

        self.days_combo.move(20, 100)


    def month(self):
        self.month_combo = QComboBox(self)

        month_label = QLabel('month', self)
        month_label.move(80, 70)

        for month in range(1, 13):
            self.month_combo.addItem(f'{month}')

        self.month_combo.move(80, 100)

    def year(self):
        self.year_combo = QComboBox(self)

        year_label = QLabel('year', self)
        year_label.move(140, 70)

        for year in range(2005, 2021):
            self.year_combo.addItem(f'{year}')

        self.year_combo.move(140, 100)

    def make_request(self):
        
        day_value = self.days_combo.currentText()
        month_value = self.month_combo.currentText()
        year_value = self.year_combo.currentText()
        self.result = self.get_result(day_value, month_value, year_value)
        self.result ["rubles"] = 1;
        try:
            output = float(self.result[self.from_cur_combo.currentText()]) * float (self.input.displayText()) / float(self.result[self.to_cur_combo.currentText()])
            self.output_value.setText(str(output))
        except:
            self.output_value.setText('x')

    def get_result(self, day, month, year):
        
        result = {
            'dollar': 0,
            'euro': 0,
        }

        if int(day) < 10:
            day = f'0{day}'
        
        if int(month) < 10:
            month = f'0{month}'

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
            result['dollar'] = dollar.text.replace(',', '.')
        except:
            result['dollar'] = 'x'

        try:
            euro = structure.find("./*[@ID='R01239']/Value")
            result['euro'] = euro.text.replace(',', '.')
        except:
            result['euro'] = 'x'

        return result

    def from_cur(self):
        self.from_cur_combo = QComboBox(self)
        self.from_cur_combo.move(30,170)
        cur_label = QLabel('From', self)
        cur_label.move(30, 150)
        self.from_cur_combo.addItem('dollar')
        self.from_cur_combo.addItem('euro')
        self.from_cur_combo.addItem('rubles')
    
    def to_cur(self):
        self.to_cur_combo = QComboBox(self)
        self.to_cur_combo.move(30,230)
        cur_label = QLabel('To', self)
        cur_label.move(30, 210)
        self.to_cur_combo.addItem('dollar')
        self.to_cur_combo.addItem('euro')
        self.to_cur_combo.addItem('rubles')

    def from_value(self):

        self.input = QLineEdit(self)
        self.input.move(130, 163)  
        ''' self.input.textChanged[str].connect(self.onChanged)
        #self.input.show()
    def onChanged(self, text):
    
        self.input_figure = text'''
        
    def load_result_image(self):

        font = QFont()
        font.setFamily('Arial')
        font.setPointSize(16)

        self.output_value = QLabel('0           ', self)
        self.output_value.setFont(font)
        self.output_value.move(130, 220)


def main():
    app = QApplication(sys.argv)
    money = CBR_API()

    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
