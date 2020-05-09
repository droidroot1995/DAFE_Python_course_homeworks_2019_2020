import requests
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QGridLayout)
from PyQt5.QtGui import (QPixmap, QPalette)
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_films(html):
    soup = BeautifulSoup(html, 'lxml')
    url = soup.find('ul', id = 'js-collection-item').find_all(class_ = 'image')

    names = []
    srcs = []

    for u in url:
        img = u.find('img')
        names.append(img.get('alt'))
        srcs.append(img.get('src'))

    return (names, srcs)
    
def get_file(url):
    resp = requests.get(url, stream=True)

    return resp

def save_data(name, file_data):
    with open(name, 'wb') as file:
        for chunk in file_data.iter_content(4096):
            file.write(chunk)

def main():
    url = 'https://www.ivi.ru/collections/movies-exciting'

    html = get_html(url)
    films = get_films(html)

    for i in range(10):
        save_data(films[0][i] + '.png', get_file(films[1][i]))

    app = QApplication([])
    w = QWidget()
    w.setWindowTitle('Films')
    w.setFixedSize(1300, 700)

    qp = QPalette()
    qp.setColor(QPalette.Window, Qt.black)
    app.setPalette(qp)

    grid = QGridLayout(w)
    
    for i in range(2):
        for j in range(5):
            label = QLabel(w)
            label.setPixmap(QPixmap(films[0][i*5 + j] + '.png'))
            grid.addWidget(label, i, j)

    w.show()

    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
