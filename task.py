import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class Password(QMainWindow):
    def __init__(self): 
        super().__init__()
        self.setGeometry(500, 500, 600, 600)
        self.setWindowTitle("Password")
        self.lb = QLabel(self)
        self.lb.setGeometry(20, 20, 560, 100)
        self.setStyleSheet("""
        font-size: 28px;
        font: Calibri;
        """)
        self.lb.setText("Parolni kiriting: ")
        self.edit_line = QLineEdit(self)
        self.edit_line.setGeometry(20,120,560,100)
        self.edit_line.setStyleSheet("""
        font-size: 28px;
        font: Calibri;
        border-color: black;
        border-width: 5px;
        border-style: solid;
        border-radius: 10px;
        """)
        self.btn = QPushButton(self)
        self.btn.setGeometry(200, 250, 200, 60)
        self.btn.setText("Kiritish")
        self.btn.setStyleSheet("""
        background-color: #000;
        color: white;
        border-color: white;
        border-width: 5px;
        border-style: solid;
        border-radius: 10px;
        """)
        self.res = QLabel(self)
        self.res.setGeometry(20, 350, 560, 100)
        self.btn.clicked.connect(self.check_password)

    def check_password(self):
        password = self.edit_line.text()
        if len(password) < 6:
            self.res.setText("Parol 6 ta belgidan kam!")
            self.res.setStyleSheet("color: red; font-size: 28px; font: Calibri;")
        else:
            a = 0
            b = 0 
            c = 0
            for x in password:
                if x.isdigit():
                    a = 1
                elif x.isalpha():
                    b = 1
                else:
                    c = 1

            if a == 1 and b == 1 and c == 1:
                self.res.setText("Parol qabul qilindi!")
                self.res.setStyleSheet("color: green; font-size: 28px; font: Calibri;")
            else:
                self.res.setText("Parol kuchli emas!")
                self.res.setStyleSheet("color: red; font-size: 28px; font: Calibri;")


if __name__ == "__main__":
    main = QApplication(sys.argv)
    new = Password()
    new.show()
    sys.exit(main.exec_())