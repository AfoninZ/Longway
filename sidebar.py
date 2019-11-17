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
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.setStyleSheet('background-color: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop: 0 #4d77b3, stop: 0.015 #67a6d0, stop: 0.03 #5578ac, stop: 1 #3364af)')

        self.gadgets = []

        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setMinimumHeight(20)

        self.clickable = QPushButton()
        self.clickable.setStyleSheet('''
                                    QPushButton {
                                        background-color: #00ffffff;
                                    }
                                    QPushButton:pressed {
                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #111166, stop: 1 #222277);     
                                    }
                                    QPushButton:hover {
                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #4685d9, stop: 1 #89c8f1);
                                    }; height: 24px; border: none; color:white; font-weight: bold;''')
        self.clickable.setText('Close Sidebar')

        self.clickable.clicked.connect(exit)
        for i in range(4):
            r = randint(0, 2)
            '''if r == 0:
                self.gadgets.append(QPushButton())
                self.gadgets[-1].setText(f'Button #{randint(0, 65535)}')
            elif r == 1:
                self.gadgets.append(QTextEdit())
                self.gadgets[-1].setText(f'Multiline #{randint(0, 65535)}')
            elif r == 2:
                self.gadgets.append(QWebEngineView())
                self.gadgets[-1].load(QUrl('https://ya.ru/'))'''
            self.gadgets.append(SidebarText())
            self.gadgets[-1].setStyleSheet('background-color:#3364af')
            # self.gadgets[-1].setFrameShape(QFrame.StyledPanel)
            self.splitter.addWidget(self.gadgets[-1])

        self.layout.addWidget(self.splitter)
        self.layout.addWidget(self.clickable)
        self.setLayout(self.layout)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

class SidebarText(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent=parent)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        self.clickable = QPushButton()
        self.clickable.setStyleSheet('''
                                    QPushButton {
                                        background-color: #00ffffff;
                                    }
                                    QPushButton:pressed {
                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #111166, stop: 1 #222277);     
                                    }
                                    QPushButton:hover {
                                        background-color: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop: 0 #4685d9, stop: 1 #89c8f1);
                                    }; height: 24px; border: none; color:white; font-weight: bold; text-align:left; padding-left:5px;''')
        self.clickable.setText('Text Edit')

        self.text = QTextEdit()
        self.text.setStyleSheet('background-color: #00ffffff; border: 1px solid #55ffffff; color:white; padding-left:5px;')

        self.layout.addWidget(self.clickable)
        self.layout.addWidget(self.text)

App = QApplication(sys.argv)
sidebar = Sidebar()
sys.exit(App.exec())