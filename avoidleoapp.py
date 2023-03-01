#!/usr/bin/python

import sys
from PyQt6.QtCore import QDate, QTime, QDateTime, Qt       # It is possible to switch to Qt5 without errors
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
import gen_simu_files
import datetime
import time

utc_offset = time.localtime().tm_gmtoff
time_now = time.time()
time_utc = time_now - utc_offset
date_time_format = "%d/%m/%Y-%H:%M:%S"
d_t_format = datetime.datetime.fromtimestamp(time_now + 5 * 60).strftime(date_time_format)

now = QDateTime.currentDateTime()

params = ()

widgets0 = []
widgets1 = []


def lst():
    num_seq_value = widgets0[1].text()
    duration_seq_value = widgets0[3].value()
    num_slots_value = widgets0[5].value()
    time_start_value = widgets0[9].dateTime().toSecsSinceEpoch()
    time_start = datetime.datetime.fromtimestamp(time_start_value).strftime(date_time_format)
    output_file_value = widgets0[7].text()
    gen_simu_files.genlst(num_seq_value, duration_seq_value, num_slots_value, time_start, output_file_value)


def besim():
    num_seq_value = widgets0[1].text()
    duration_seq_value = widgets0[3].value()
    num_slots_value = widgets0[5].value()
    time_start_value = widgets0[9].dateTime().toSecsSinceEpoch()
    time_start = datetime.datetime.fromtimestamp(time_start_value).strftime(date_time_format)
    output_file_value = widgets0[7].text()
    gen_simu_files.genjson(num_seq_value, duration_seq_value, num_slots_value, time_start, output_file_value)


class AvoidLeoWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        global params
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
        lst_button.resize(lst_button.sizeHint())
        widgets1.append(lst_button)

        besim_button = QPushButton("Generate .json for LaReunion besim", self)
        besim_button.setCheckable(True)
        besim_button.resize(besim_button.sizeHint())
        widgets1.append(besim_button)

        lst_button.clicked.connect(lst)
        besim_button.clicked.connect(besim)

    def genparams(self):
        num_seq = QLineEdit("6940", self)
        seq_label = QLabel("Binary sequence name or number (ex: 6940, etc.):", self)
        duration_seq = QSpinBox()
        duration_seq.setMaximum(200)
        duration_seq.setMinimum(1)
        duration_seq.setValue(12)
        duration_label = QLabel("Duration of the sequence in minutes:", self)
        num_slots = QSpinBox()
        num_slots.setMaximum(1000)
        num_slots.setMinimum(1)
        num_slots.setValue(40)
        slots_label = QLabel("Number of slots/repetition of the sequence:", self)
        output_file = QLineEdit("default")
        file_label = QLabel("Name of the output file (without extension):", self)
        offset = ""
        if utc_offset >= 0:
            offset = "+"
        elif utc_offset < 0:
            offset = "-"
        offset = offset + str(utc_offset / 3600)
        cal = QDateTimeEdit(QDateTime.fromSecsSinceEpoch(int(time_utc)), self)
        cal.setCalendarPopup(True)
        callabel = QLabel("Starting date and UTC time (Your computer is UTC" + offset + "H):", self)
        callabel.setBuddy(cal)
        widgets0.extend([seq_label, num_seq,
                         duration_label, duration_seq,
                         slots_label, num_slots,
                         file_label, output_file,
                         callabel, cal])
        # return num_seq.text(), duration_seq.value(), num_slots.value, time_start, output_file.text()


def main():
    app = QApplication(sys.argv)
    ex = AvoidLeoWindow()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
