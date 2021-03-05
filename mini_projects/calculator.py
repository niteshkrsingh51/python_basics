import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel , QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = QWidget()
    w.resize(300,300)
    w.setWindowTitle('Calculator')
    label = QLabel(w)
    label.setText("Enter the number: ")
    label.show()
    w.Textbox = QLineEdit(w)
    w.Textbox.move(0, 20)
    w.show()
    sys.exit(app.exec_())