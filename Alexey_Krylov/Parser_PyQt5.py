#!/usr/bin/python3

import sys

import webbrowser
import lxml.etree as ET
import urllib.request
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QHBoxLayout, QLineEdit, QComboBox
from PyQt5.QtGui import QPixmap, QFont, QPalette


class Parser(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        self.tx = QLabel(self)
        self.tx.setText('Выберите интересующую вас тему: ')
        self.tx.move(4, 130)
        self.op = QComboBox(self)
        self.op.addItems(['Главное', 'Коронавирус', 'Политика',
                         'Общество', 'Экономика', 'В мире', 'Спорт', 'Происшествия', 
                         'Культура', 'Технологии', 'Наука', 'Авто'])
        self.op.move(2, 150)
        self.op.resize(220, 30)

        self.btn = QPushButton(self)
        self.btn.setText('Смотреть')
        self.btn.move(220, 150)
        self.btn.resize(100, 30)
        self.btn.clicked.connect(self.dialog)


        self.resize(350, 350)
        self.setWindowTitle('Новости')
        self.show()

    def get_news(self, text):
        rubrics = {'Главное' : 'index',
               'Коронавирус' : 'koronavirus',
               'Политика' : 'politics',
               'Общество' : 'society',
               'Экономика' : 'business',
               'В мире' : 'world',
               'Спорт' : 'sport',
               'Происшествия' : 'incident',
               'Культура' : 'culture',
               'Технологии' : 'computers',
               'Наука' : 'science',
               'Авто' : 'auto'}

        rubric = rubrics[text]
        res = dict()

        if rubric == 'sport':
            url = urllib.request.urlopen('https://yandex.ru/sport')
        else:
            url = urllib.request.urlopen(f'https://yandex.ru/news/rubric/{rubric}')
 
        data = url.read().decode('utf-8').split('story/')

        for i in range(1, min(len(data), 30)):
            if rubric == 'sport':
                current_link = 'https://yandex.ru/sport/story/' + data[i][:data[i].find('?lang=')]
            else:
                current_link = 'https://yandex.ru/news/story/' + data[i][:data[i].find('?lr=')]
            url = urllib.request.urlopen(current_link)
            header = url.read().decode('utf-8').split('<title>')
            if rubric == 'sport':
                res.update({header[1][:header[1].find(': Яндекс.Спорт')] : current_link})
            else:
                res.update({header[1][:header[1].find(': Яндекс.Новости')] : current_link})
        return res


    def dialog(self):

        opp = self.op.currentText()

        self.new_window = QWidget()

        self.news = self.get_news(opp)

        self.op2 = QComboBox(self.new_window)
        self.op2.move(0, 170)
        self.op2.addItems(self.news.keys())
        
        self.btn2 = QPushButton(self.new_window)
        self.btn2.setText('Перейти')
        self.btn2.move(413, 195)
        self.btn2.clicked.connect(self.Go_to_artickle)

        self.new_window.resize(517, 400)
        self.new_window.setWindowTitle(f'Статьи: {opp}')
        self.new_window.show()
  
    def Go_to_artickle(self):
        opp2 = self.op2.currentText()
        webbrowser.open(self.news[opp2], new=1)



def main():
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    pars = Parser()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()


