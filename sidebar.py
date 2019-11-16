from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLineEdit, QVBoxLayout, QSplitter, QPushButton, QTextEdit
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtCore import *
from random import randint

class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle = "Longway Sidebar"
        self.setGeometry(1366 - 180, 0, 180, 768)

        self.layout = QVBoxLayout()
        self.layout.setContentsMargins(5, 5, 5, 5)
        self.setStyleSheet('background-color:#222277')

        self.gadgets = []

        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setMinimumHeight(20)

        self.combobox = QPushButton()
        self.combobox.setText('Close Sidebar')
        self.combobox.setFixedHeight(20)

        self.combobox.clicked.connect(exit)
        for i in range(7):
            r = randint(0, 2)
            if r == 0:
                self.gadgets.append(QPushButton())
                self.gadgets[-1].setText(f'Button #{randint(0, 65535)}')
            elif r == 1:
                self.gadgets.append(QTextEdit())
                self.gadgets[-1].setText(f'Multiline #{randint(0, 65535)}')
            elif r == 2:
                self.gadgets.append(QWebEngineView())
                self.gadgets[-1].load(QUrl('https://ya.ru/'))
            self.gadgets[-1].setStyleSheet('background-color:#5555dd')
            # self.gadgets[-1].setFrameShape(QFrame.StyledPanel)
            self.splitter.addWidget(self.gadgets[-1])

        self.layout.addWidget(self.splitter)
        self.layout.addWidget(self.combobox)
        self.setLayout(self.layout)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

App = QApplication(sys.argv)
sidebar = Sidebar()
sys.exit(App.exec())