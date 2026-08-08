import os
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys

class calc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(550, 80, 800, 920)
        self.setWindowTitle("Calculator")
        self.setStyleSheet("""
        background-color: rgb(0,0,0);
        border-radius: 20px;
        font-size: 25px;
        """)
        self.inp = QLineEdit(self)
        self.inp.setGeometry(50, 50, 700, 100)
        self.inp.setStyleSheet("""
        font: Calibri;
        font-size: 60px;
        color: #fff;
        """)
        self.main = QLabel(self)
        self.main.setGeometry(50, 160, 700, 720)
        self.n1 = QPushButton(self.main)
        self.n1.setText("AC")
        self.n1.setGeometry(30, 20, 120, 120)
        self.n1.setStyleSheet("""
                color: white;
                border: 0;
                background-color: grey;
                border-radius: 50%;
        """)
        self.n1.clicked.connect(self.clear)
        self.n2 = QPushButton(self.main)
        self.n2.setText("+/-")
        self.n2.setGeometry(200, 20, 120, 120)
        self.n2.setStyleSheet("""
                color: white;
                border: 0;
                background-color: grey;
                border-radius: 50%;
        """)
        self.n2.clicked.connect(lambda: self.press(self.n2.text()))
        self.n3 = QPushButton(self.main)
        self.n3.setText("%")
        self.n3.setGeometry(370, 20, 120, 120)
        self.n3.setStyleSheet("""
                color: white;
                border: 0;
                background-color: grey;
                border-radius: 50%;
        """)
        self.n3.clicked.connect(lambda: self.press(self.n3.text()))
        self.n4 = QPushButton(self.main)
        self.n4.setText("//")
        self.n4.setGeometry(530, 20, 120, 120)
        self.n4.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #ff9500;
                border-radius: 50%;
        """)
        self.n4.clicked.connect(lambda: self.press(self.n4.text()))

        self.n5 = QPushButton(self.main)
        self.n5.setText("7")
        self.n5.setGeometry(30, 160, 120, 120)
        self.n5.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n5.clicked.connect(lambda: self.press(self.n5.text()))
        self.n6 = QPushButton(self.main)
        self.n6.setText("8")
        self.n6.setGeometry(200, 160, 120, 120)
        self.n6.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n6.clicked.connect(lambda: self.press(self.n6.text()))
        self.n7 = QPushButton(self.main)
        self.n7.setText("9")
        self.n7.setGeometry(370, 160, 120, 120)
        self.n7.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n7.clicked.connect(lambda: self.press(self.n7.text()))
        self.n8 = QPushButton(self.main)
        self.n8.setText("x")
        self.n8.setGeometry(530, 160, 120, 120)
        self.n8.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #ff9500;
                border-radius: 50%;
        """)
        self.n8.clicked.connect(lambda: self.press(self.n8.text()))

        self.n9 = QPushButton(self.main)
        self.n9.setText("4")
        self.n9.setGeometry(30, 300, 120, 120)
        self.n9.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n9.clicked.connect(lambda: self.press(self.n9.text()))
        self.n10 = QPushButton(self.main)
        self.n10.setText("5")
        self.n10.setGeometry(200, 300, 120, 120)
        self.n10.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n10.clicked.connect(lambda: self.press(self.n10.text()))
        self.n11 = QPushButton(self.main)
        self.n11.setText("6")
        self.n11.setGeometry(370, 300, 120, 120)
        self.n11.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n11.clicked.connect(lambda: self.press(self.n11.text()))
        self.n12 = QPushButton(self.main)
        self.n12.setText("-")
        self.n12.setGeometry(530, 300, 120, 120)
        self.n12.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #ff9500;
                border-radius: 50%;
        """)
        self.n12.clicked.connect(lambda: self.press(self.n12.text()))

        self.n13 = QPushButton(self.main)
        self.n13.setText("1")
        self.n13.setGeometry(30, 440, 120, 120)
        self.n13.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n13.clicked.connect(lambda: self.press(self.n13.text()))
        self.n14 = QPushButton(self.main)
        self.n14.setText("2")
        self.n14.setGeometry(200, 440, 120, 120)
        self.n14.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n14.clicked.connect(lambda: self.press(self.n14.text()))
        self.n15 = QPushButton(self.main)
        self.n15.setText("3")
        self.n15.setGeometry(370, 440, 120, 120)
        self.n15.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n15.clicked.connect(lambda: self.press(self.n15.text()))
        self.n16 = QPushButton(self.main)
        self.n16.setText("+")
        self.n16.setGeometry(530, 440, 120, 120)
        self.n16.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #ff9500;
                border-radius: 50%;
        """)
        self.n16.clicked.connect(lambda: self.press(self.n16.text()))

        self.n17 = QPushButton(self.main)
        self.n17.setText("0")
        self.n17.setGeometry(30, 580, 290, 120)
        self.n17.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 60px;
        """)
        self.n17.clicked.connect(lambda: self.press(self.n17.text()))
        self.n18 = QPushButton(self.main)
        self.n18.setText(".")
        self.n18.setGeometry(370, 580, 120, 120)
        self.n18.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #333333;
                border-radius: 50%;
        """)
        self.n18.clicked.connect(lambda: self.press(self.n18.text()))
        self.n19 = QPushButton(self.main)
        self.n19.setText("=")
        self.n19.setGeometry(530, 580, 120, 120)
        self.n19.setStyleSheet("""
                color: white;
                border: 0;
                background-color: #ff9500;
                border-radius: 50%;
        """)

    def press(self, value):
        self.inp.setText(self.inp.text() + value)

    def clear(self):
        self.inp.setText("")


if __name__ == "__main__":
    main = QApplication(sys.argv)
    new = calc()
    new.show()
    sys.exit(main.exec_())