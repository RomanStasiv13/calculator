from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow

from controller import Control

app = QApplication([])
window = QMainWindow()
c = Control(window)
app.exec_()

