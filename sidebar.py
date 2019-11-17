from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLineEdit, QVBoxLayout, QSplitter, QPushButton, QTextEdit
from PyQt5.QtWebEngineWidgets import *
import sys
from PyQt5.QtCore import *
from random import randint
import subprocess
import os

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
        self.clickable.setText('Add Gadget')

        self.clickable.clicked.connect(self.add_gadget)
        for i in range(0):
            r = randint(0, 1)
            if r == 0:
                self.gadgets.append(GadgetText())
            elif r == 1:
                self.gadgets.append(GadgetWeb())
            # self.gadgets[-1].setFrameShape(QFrame.StyledPanel)
            self.splitter.addWidget(self.gadgets[-1])

        self.layout.addWidget(self.splitter)
        self.layout.addWidget(self.clickable)
        self.setLayout(self.layout)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.show()

    def add_gadget(self):
        self.gadgets.append(GadgetLaunch([('sudo apt-get update', 'Windows Store'), ('gnome-terminal', 'gnome-terminal')]))
        self.splitter.addWidget(self.gadgets[-1])

class Gadget(QWidget):
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
        self.clickable.setText('Sidebar Gadget')

        self.layout.addWidget(self.clickable)

class GadgetText(Gadget):
    def __init__(self, parent=None):
        Gadget.__init__(self, parent=parent)

        self.clickable.setText('Text Edit')

        self.text = QTextEdit()
        self.text.setStyleSheet('background-color: #00ffffff; border: 1px solid #55ffffff; color:white; padding-left:5px;')

        self.layout.addWidget(self.text)

class GadgetWeb(Gadget):
    def __init__(self, parent=None):
        Gadget.__init__(self, parent=parent)

        self.clickable.setText('Web Browser')

        self.browser = QWebEngineView()
        self.browser.load(QUrl('https://ya.ru/'))

        self.layout.addWidget(self.browser)

class GadgetLaunch(Gadget):
    def __init__(self, links, parent=None):
        Gadget.__init__(self, parent=parent)

        self.clickable.setText('Quick Launch')

        self.launchers = []
        for link in links:
            self.launchers.append(QPushButton())
            self.launchers[-1].setStyleSheet('''
                                    QPushButton {
                                        background-color: #00000000;
                                    }
                                    QPushButton:pressed {
                                        background-color: #aa000000;     
                                    }
                                    QPushButton:hover {
                                        background-color: #55000000;
                                    } height: 24px; border: none; color:white; font-weight: bold; text-align:left; padding-left:5px;''')
            print(link)
            self.launchers[-1].setText(link[1])
            self.launchers[-1].clicked.connect(lambda a: os.system(link[0]))

            self.layout.addWidget(self.launchers[-1])
        self.layout.addStretch()

App = QApplication(sys.argv)
sidebar = Sidebar()
sys.exit(App.exec())
