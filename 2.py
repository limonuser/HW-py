import sys
import json
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Employee Management")
        self.resize(420, 620)

        with open("info.json", "r", encoding="utf-8") as f:
            self.data = json.load(f)

        self.departments = self.data["departments"]
        self.employees = self.data["employees"]
        self.selected_employee = None

        self.title_lbl = QLabel("Employee Management", self)
        self.title_lbl.setAlignment(Qt.AlignCenter)
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.title_lbl.setFont(font)

        self.search_inp = QLineEdit(self)
        self.search_inp.setPlaceholderText("Enter employee fullname")

        self.search_btn = QPushButton("Search Employee", self)

        self.fullname_inp = QLineEdit(self)
        self.fullname_inp.setPlaceholderText("Full Name")

        self.age_inp = QLineEdit(self)
        self.age_inp.setPlaceholderText("Age")

        self.phone_inp = QLineEdit(self)
        self.phone_inp.setPlaceholderText("+998901234567")

        self.email_inp = QLineEdit(self)
        self.email_inp.setPlaceholderText("Email Address")

        self.gender_combo = QComboBox(self)
        self.gender_combo.addItems(["Male", "Female"])

        self.dept_combo = QComboBox(self)
        self.dept_combo.addItems(self.departments)

        self.edit_btn = QPushButton("Edit Employee", self)

        self.search_btn.clicked.connect(self.search_employee)
        self.edit_btn.clicked.connect(self.edit_employee)

        layout = QVBoxLayout(self)
        layout.addWidget(self.title_lbl)
        layout.addWidget(self.search_inp)
        layout.addWidget(self.search_btn)
        layout.addWidget(self.fullname_inp)
        layout.addWidget(self.age_inp)
        layout.addWidget(self.phone_inp)
        layout.addWidget(self.email_inp)
        layout.addWidget(self.gender_combo)
        layout.addWidget(self.dept_combo)
        layout.addWidget(self.edit_btn)

    def search_employee(self):
        searched_name = self.search_inp.text().strip()

        if searched_name == "":
            QMessageBox.warning(self, "Error", "Iltimos ism kiriting")
            return

        find = None
        for emp in self.employees:
            if emp["fullname"].lower() == searched_name.lower():
                find = emp
                break

        if find is None:
            QMessageBox.warning(self, "Error", "Employee topilmadi")
            return

        self.selected_employee = find

        self.fullname_inp.setText(find["fullname"])
        self.age_inp.setText(str(find["age"]))
        self.phone_inp.setText(find["phone"])
        self.email_inp.setText(find["email"])

        gender_index = self.gender_combo.findText(find["gender"])
        self.gender_combo.setCurrentIndex(gender_index)

        self.dept_combo.setCurrentIndex(find["department_index"])

    def edit_employee(self):
        if self.selected_employee is None:
            QMessageBox.warning(self, "Error", "Avval employee ni qidiring")
            return

        self.selected_employee["fullname"] = self.fullname_inp.text()
        self.selected_employee["age"] = int(self.age_inp.text())
        self.selected_employee["phone"] = self.phone_inp.text()
        self.selected_employee["email"] = self.email_inp.text()
        self.selected_employee["gender"] = self.gender_combo.currentText()
        self.selected_employee["department_index"] = self.dept_combo.currentIndex()

        with open("info.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, indent=4, ensure_ascii=False)

        QMessageBox.information(self, "Success", "Employee updated successfully")


if __name__ == "__main__":
    main = QApplication([])
    app = window()
    app.show()
    sys.exit(main.exec_())
