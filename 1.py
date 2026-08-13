import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sevimli mashg'ulotlar")
        self.resize(400, 550)

        self.name_lbl = QLabel("Ism", self)
        self.name_inp = QLineEdit(self)

        self.age_lbl = QLabel("Yoshi", self)
        self.age_inp = QLineEdit(self)

        self.hobby_lbl = QLabel("Sevimli mashg'ulotlar", self)
        self.futbol_chk = QCheckBox("Futbol", self)
        self.kitob_chk = QCheckBox("Kitob o'qish", self)
        self.musiqa_chk = QCheckBox("Musiqa", self)
        self.rasm_chk = QCheckBox("Rasm chizish", self)
        self.sayohat_chk = QCheckBox("Sayohat", self)

        self.gender_lbl = QLabel("Jinsi", self)
        self.erkak_rad = QRadioButton("Erkak", self)
        self.ayol_rad = QRadioButton("Ayol", self)
        self.gender_group = QButtonGroup(self)
        self.gender_group.addButton(self.erkak_rad)
        self.gender_group.addButton(self.ayol_rad)

        self.add_btn = QPushButton("Qo'shish", self)
        self.edit_btn = QPushButton("Tahrirlash", self)
        self.delete_btn = QPushButton("O'chirish", self)

        self.output_list = QListWidget(self)

        self.add_btn.clicked.connect(self.add_item)
        self.edit_btn.clicked.connect(self.edit_item)
        self.delete_btn.clicked.connect(self.delete_item)

        layout = QVBoxLayout(self)
        layout.addWidget(self.name_lbl)
        layout.addWidget(self.name_inp)
        layout.addWidget(self.age_lbl)
        layout.addWidget(self.age_inp)

        layout.addWidget(self.hobby_lbl)
        layout.addWidget(self.futbol_chk)
        layout.addWidget(self.kitob_chk)
        layout.addWidget(self.musiqa_chk)
        layout.addWidget(self.rasm_chk)
        layout.addWidget(self.sayohat_chk)

        layout.addWidget(self.gender_lbl)
        gender_layout = QHBoxLayout()
        gender_layout.addWidget(self.erkak_rad)
        gender_layout.addWidget(self.ayol_rad)
        layout.addLayout(gender_layout)

        btn_layout = QHBoxLayout()
        btn_layout.addWidget(self.add_btn)
        btn_layout.addWidget(self.edit_btn)
        btn_layout.addWidget(self.delete_btn)
        layout.addLayout(btn_layout)

        layout.addWidget(self.output_list)

  

if __name__ == "__main__":
    main = QApplication([])
    app = window()
    app.show()
    sys.exit(main.exec_())
