"""this script is gay"""
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit

statement = ""
pos = -1
char = ''

def next_char():
    """set char to next one in statement"""
    global char
    global pos
    pos += 1
    if pos < len(statement):
        char = statement[pos]
    else:
        char = 'z'

def eat_char(char_to_eat):
    """advance the position forward if characters match"""
    global char
    if char == char_to_eat:
        next_char()
        return True
    else:
        return False

def get_expression():
    """get results separated by + and -"""
    result = get_term()
    while True:
        if eat_char("+"):
            result += get_term()
        elif eat_char("-"):
            result -= get_term()
        else:
            return result

def get_term():
    """get results separated by * and /"""
    result = get_factor()
    while True:
        if eat_char("*"):
            result *= get_factor()
        elif eat_char("/"):
            result /= get_factor()
        else:
            return result

def get_factor():
    """read numbers and parentheses"""
    global char
    if eat_char("+"):
        return get_factor()
    if eat_char("-"):
        return -get_factor()

    result = 0
    number = ""
    if eat_char("("):
        result = get_expression()
        eat_char(")")
    elif ((ord(char) >= ord('0') and ord(char) <= ord('9')) or char == '.'):
        while ((ord(char) >= ord('0') and ord(char) <= ord('9')) or char == '.'):
            number = number + char
            next_char()
        result = float(number)
    return result


def clear_one(textbox):
    """clears one character from statement"""
    global statement
    statement = statement[:-1]
    textbox.setText(statement)

def clear_all(textbox):
    """clears all characters from statement"""
    global statement
    statement = ""
    textbox.setText(statement)

def change_sign(textbox):
    """negates whole statement"""
    global statement
    statement = "-(" + statement + ")"
    textbox.setText(statement)

def evaluate(textbox):
    """evaluates statement"""
    global statement
    global pos
    pos = -1
    next_char()
    result = get_expression()
    statement = str(result)
    textbox.setText(statement)

def add_character(string, textbox):
    """adds specified char to statement"""

    global statement
    if (statement == '0' or statement == "0.0"):
        statement = ""
    statement += string
    textbox.setText(statement)

def main():
    """pims"""

    app = QApplication(sys.argv)
    window = QWidget()
    window.resize(700, 700)
    window.setWindowTitle("Coolculator")

    button1 = QPushButton(window)
    button1.setText("1")
    button1.move(100, 400)
    button1.setFixedSize(75, 75)
    button1.show()
    button2 = QPushButton(window)
    button2.setText("2")
    button2.move(200, 400)
    button2.setFixedSize(75, 75)
    button2.show()
    button3 = QPushButton(window)
    button3.setText("3")
    button3.move(300, 400)
    button3.setFixedSize(75, 75)
    button3.show()
    button4 = QPushButton(window)
    button4.setText("4")
    button4.move(100, 300)
    button4.setFixedSize(75, 75)
    button4.show()
    button5 = QPushButton(window)
    button5.setText("5")
    button5.move(200, 300)
    button5.setFixedSize(75, 75)
    button5.show()
    button6 = QPushButton(window)
    button6.setText("6")
    button6.move(300, 300)
    button6.setFixedSize(75, 75)
    button6.show()
    button7 = QPushButton(window)
    button7.setText("7")
    button7.move(100, 200)
    button7.setFixedSize(75, 75)
    button7.show()
    button8 = QPushButton(window)
    button8.setText("8")
    button8.move(200, 200)
    button8.setFixedSize(75, 75)
    button8.show()
    button9 = QPushButton(window)
    button9.setText("9")
    button9.move(300, 200)
    button9.setFixedSize(75, 75)
    button9.show()
    button0 = QPushButton(window)
    button0.setText("0")
    button0.move(100, 500)
    button0.setFixedSize(175, 75)
    button_left_parenthesis = QPushButton(window)
    button_left_parenthesis.setText("(")
    button_left_parenthesis.move(100, 600)
    button_left_parenthesis.setFixedSize(175, 75)
    button_right_parenthesis = QPushButton(window)
    button_right_parenthesis.setText(")")
    button_right_parenthesis.move(300, 600)
    button_right_parenthesis.setFixedSize(175, 75)
    button_point = QPushButton(window)
    button_point.setText(".")
    button_point.move(300, 500)
    button_point.setFixedSize(75, 75)
    button_plus = QPushButton(window)
    button_plus.setText("+")
    button_plus.move(400, 500)
    button_plus.setFixedSize(75, 75)
    button_plus.show()
    button_minus = QPushButton(window)
    button_minus.setText("-")
    button_minus.move(400, 400)
    button_minus.setFixedSize(75, 75)
    button_minus.show()
    button_multiply = QPushButton(window)
    button_multiply.setText("*")
    button_multiply.move(400, 300)
    button_multiply.setFixedSize(75, 75)
    button_multiply.show()
    button_divide = QPushButton(window)
    button_divide.setText("/")
    button_divide.move(400, 200)
    button_divide.setFixedSize(75, 75)
    button_divide.show()
    button_equals = QPushButton(window)
    button_equals.setText("=")
    button_equals.move(500, 500)
    button_equals.setFixedSize(75, 175)
    button_equals.show()
    button_clear = QPushButton(window)
    button_clear.setText("C")
    button_clear.move(500, 400)
    button_clear.setFixedSize(75, 75)
    button_clear.show()
    button_clear_everything = QPushButton(window)
    button_clear_everything.setText("CE")
    button_clear_everything.move(500, 300)
    button_clear_everything.setFixedSize(75, 75)
    button_clear_everything.show()
    button_sign = QPushButton(window)
    button_sign.setText("+/-")
    button_sign.move(500, 200)
    button_sign.setFixedSize(75, 75)
    button_sign.show()

    textbox = QLineEdit(window)
    textbox.move(100, 100)
    textbox.resize(500, 40)
    textbox.setReadOnly(True)
    textbox.setAlignment(Qt.AlignRight)
    textbox.show()

    button1.clicked.connect(lambda: add_character("1", textbox))
    button2.clicked.connect(lambda: add_character("2", textbox))
    button3.clicked.connect(lambda: add_character("3", textbox))
    button4.clicked.connect(lambda: add_character("4", textbox))
    button5.clicked.connect(lambda: add_character("5", textbox))
    button6.clicked.connect(lambda: add_character("6", textbox))
    button7.clicked.connect(lambda: add_character("7", textbox))
    button8.clicked.connect(lambda: add_character("8", textbox))
    button9.clicked.connect(lambda: add_character("9", textbox))
    button_plus.clicked.connect(lambda: add_character("+", textbox))
    button_minus.clicked.connect(lambda: add_character("-", textbox))
    button_multiply.clicked.connect(lambda: add_character("*", textbox))
    button_divide.clicked.connect(lambda: add_character("/", textbox))
    button_equals.clicked.connect(lambda: evaluate(textbox))
    button_clear.clicked.connect(lambda: clear_one(textbox))
    button_clear_everything.clicked.connect(lambda: clear_all(textbox))
    button_sign.clicked.connect(lambda: change_sign(textbox))
    button0.clicked.connect(lambda: add_character("0", textbox))
    button_left_parenthesis.clicked.connect(lambda: add_character("(", textbox))
    button_right_parenthesis.clicked.connect(lambda: add_character(")", textbox))
    button_point.clicked.connect(lambda: add_character(".", textbox))

    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
