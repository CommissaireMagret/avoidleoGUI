#!/usr/bin/python

import sys
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
from PyQt6.QtWidgets import QWidget, QMessageBox, QApplication, QPushButton, QMainWindow, QDateTimeEdit, QVBoxLayout, \
    QHBoxLayout
import lstgen
import besimgen

now = QDateTime.currentDateTime()

widgets0 = []
widgets1 = []

class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle("Avoid LEO SAR satellites")

        layout = QVBoxLayout()
        layout0 = QVBoxLayout()
        layout1 = QHBoxLayout()

        self.genparams()
        self.buttons()

        for w in widgets0:
            layout0.addWidget(w)
        for w in widgets1:
            layout1.addWidget(w)
        layout.addLayout(layout0)
        layout.addLayout(layout1)
        widget = QWidget()
        widget.setLayout(layout)
        self.setGeometry(300, 300, 350, 200)
        self.resize(350, 250)
        self.setCentralWidget(widget)
        self.center()
        self.show()

    def closeEvent(self, event):

        reply = QMessageBox.question(self, 'Message',
                                     "Are you sure to quit?", QMessageBox.StandardButton.Yes |
                                     QMessageBox.StandardButton.No, QMessageBox.StandardButton.No)

        if reply == QMessageBox.StandardButton.Yes:

            event.accept()
        else:

            event.ignore()

    def center(self):

        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()

        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def buttons(self):
        lst_button = QPushButton("Generate .lst for TLS simulator", self)
        lst_button.setCheckable(True)
        lst_button.clicked.connect(self.the_button_was_clicked)
        lst_button.resize(lst_button.sizeHint())
        widgets1.append(lst_button)

        besim_button = QPushButton("Generate .json for LaReunion besim", self)
        besim_button.setCheckable(True)
        besim_button.clicked.connect(self.the_button_was_clicked)
        besim_button.resize(besim_button.sizeHint())
        widgets1.append(besim_button)

    def the_button_was_clicked(self):
        print("Clicked!")

    def genparams(self):
        cal = QDateTimeEdit(now.toUTC())
        cal.setCalendarPopup(True)
        widgets0.append(cal)


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
