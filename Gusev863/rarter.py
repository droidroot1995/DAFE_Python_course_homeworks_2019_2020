import requests
import traceback
import sys
import time
from PyQt5 import QtGui
from PyQt5.QtCore import Qt, QUrl, QRunnable, QObject
from PyQt5.QtWidgets import (QWidget, QLabel, QApplication, QPushButton, QMessageBox, QLineEdit)
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def get_header(html):
    soup = BeautifulSoup(html, 'lxml')
    threads = soup.find_all('div', {"class":"postInfo desktop"})

    headers = []
    names = []
    for t in threads:
        name = t.find('input')
        header = t.find_all('span', {"class": "subject"})
        if (len(header) == 1):
            names.append(name.get("name"))
        for h in header:
            headers.append(h.string)
    
    return headers, names

def open_url(thread_url, window):
    url = QUrl(thread_url)
    if not QtGui.QDesktopServices.openUrl(url):
        QMessageBox.warning(window, 'Open Url', 'Could not find thread')

def find_thread(short_name):
    url = 'https://boards.4channel.org/vg/'

    page_number = 0

    html = get_html(url)
    headers, names = get_header(html)
    thread_url = ""
    i = 0
    for h in headers:
        text = h.split()
        if (text[0] == '/' + short_name + '/'):
            thread_url = "https://boards.4channel.org/vg/thread/" + names[i]
            print(thread_url)
            page_number = 1
        i += 1

    if (thread_url != ""):
        return thread_url, page_number

    for i in range(2, 11):
        url = 'https://boards.4channel.org/vg/'+str(i)
        html = get_html(url)
        headers, names = get_header(html)
        j = 0
        for h in headers:
            text = h.split()
            if (text[0] == '/' + short_name + '/'):
                thread_url = "https://boards.4channel.org/vg/thread/" + names[j]
                page_number = i
                print(thread_url)
            j += 1
        if (thread_url != ""):
            return thread_url, page_number
    return thread_url, page_number

def update_button(textbox, button, label, window):
    text = textbox.text()
    thread_url, page_number = find_thread(text)
    if (thread_url != ""):
        label.setText("Found /" + text + "/ on page " + str(page_number) + "!")
        button.setText("/" + text + "/")
    else:
        label.setText("Couldn't Find /" + text + "/")
        button.setText("Not Found")
    button.disconnect()
    button.clicked.connect(lambda: open_url(thread_url, window))

def main():
    thread_url, page_number = find_thread("rlg")

    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle('4chan thread finder')
    window.setFixedSize(700, 700)

    textbox = QLineEdit(window)
    textbox.move(100, 100)
    textbox.resize(500, 40)
    textbox.show()

    button = QPushButton(window)
    if (thread_url != ""):
        button.setText("/rlg/")
    else:
        button.setText("Not Found")
    button.move(400, 300)
    button.setFixedSize(100, 100)
    button.show()

    button_search = QPushButton(window)
    button_search.setText("search")
    button_search.move(200, 300)
    button_search.setFixedSize(100, 100)
    button_search.show()

    label = QLabel(window)
    if (thread_url != ""):
        label.setText("Found /rlg/ on page " + str(page_number) + "!")
    else:
        label.setText("Couldn't find /rlg/")
    label.move(300, 200)
    label.setFixedSize(300, 50)
    label.show()

    button.clicked.connect(lambda: open_url(thread_url, window))
    button_search.clicked.connect(lambda: update_button(textbox, button, label, window))

    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()