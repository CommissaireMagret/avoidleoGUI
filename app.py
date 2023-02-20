from PyQt6.QtWidgets import QApplication, QWidget

import sys
import argparse

app = QApplication(sys.argv)

# Create a Qt widget, which will be our window.
window = QWidget()
window.show()  # IMPORTANT!!!!! Windows are hidden by default.

app.exec()