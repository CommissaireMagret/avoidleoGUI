#!/usr/bin/python

import sys
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt
from PyQt6.QtWidgets import (
    QWidget,
    QMessageBox,
    QApplication,
    QPushButton,
    QMainWindow,
    QDateTimeEdit,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QSpinBox,
)
import lstgen
import besimgen
import datetime
import time

utc_offset = time.localtime().tm_gmtoff
time_now = time.time()
time_utc = time_now - utc_offset

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
        lst_button.clicked.connect(self.lstgen)
        lst_button.resize(lst_button.sizeHint())
        widgets1.append(lst_button)

        besim_button = QPushButton("Generate .json for LaReunion besim", self)
        besim_button.setCheckable(True)
        besim_button.clicked.connect(self.besimgen)
        besim_button.resize(besim_button.sizeHint())
        widgets1.append(besim_button)

    def lstgen(self):
        lstgen.genlst(self.num_seq, duration_seq, num_cren, file="default",time_start)
    def besimgen(self):
        print("besim!")

    def genparams(self):
        num_seq = QLineEdit("6940")
        seq_label = QLabel("Binary sequence name or number (ex: 6940, etc.):")
        duration_seq = QSpinBox()
        duration_label = QLabel("Duration of the sequence in minutes:")
        num_slots = QSpinBox()
        slots_label = QLabel("Number of slots/repetition of the sequence:")
        output_file = QLineEdit("")
        file_label = QLabel("Name of the output file (without extension):")
        offset = ""
        if utc_offset >= 0:
            offset = "+"
        elif utc_offset < 0:
            offset = "-"
        offset = offset + str(utc_offset/3600)
        cal = QDateTimeEdit(QDateTime.fromSecsSinceEpoch(int(time_utc)))
        cal.setCalendarPopup(True)
        callabel = QLabel("Starting date and UTC time (Your computer is UTC" + offset + "H):")
        callabel.setBuddy(cal)
        widgets0.extend([seq_label, num_seq,
                         duration_label, duration_seq,
                         slots_label, num_slots,
                         file_label, output_file,
                         callabel, cal])


def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
