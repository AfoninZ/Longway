from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSplitter, QLabel
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen, QBrush, QLinearGradient, QImage
from PyQt5.QtCore import *
import sys

import aero


class Sidebar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle = "Longway Sidebar"
        self.setGeometry(1920 - 180, 0, 180, 1080 - 32)

        self.color_gradient_left = QColor(100, 100, 100, 50)
        self.color_gradient_right = QColor(0, 0, 0, 255)

        self.layout = QVBoxLayout()
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # self.layout.addWidget(QWidget())
        self.setLayout(self.layout)

        # Splitter for storing gadgets
        self.gadgets = []

        self.splitter = QSplitter(Qt.Vertical)
        self.splitter.setChildrenCollapsible(False)
        self.splitter.setMinimumHeight(20)
        self.splitter.setStyleSheet('''
                                    QSplitter::handle:vertical {
                                        height: 1px;
                                        background: black
                                    }''')
        self.layout.addWidget(self.splitter)

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        # Starting the show!
        self.addGadget(GadgetObama())
        self.addGadget(Gadget())
        self.addGadget(Gadget())
        self.addGadget(Gadget())
        self.addGadget(QWidget())
        self.show()

    def paintEvent(self, event):
        # Initializing QPainter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        sidebar_rect = self.geometry()
        # Gradient
        gradient = QLinearGradient(0, 0, sidebar_rect.width(), 0)
        gradient.setColorAt(0.0, self.color_gradient_left)
        gradient.setColorAt(1.0, self.color_gradient_right)

        qp.setBrush(QBrush(gradient))
        # qp.setPen(Qt.white)
        qp.drawRect(0, 0, sidebar_rect.width(), sidebar_rect.height())

        # Glass highlight
        qp.setBrush(QBrush(Qt.white))
        qp.setPen(QPen(QBrush(Qt.white), 0.01))
        qp.setOpacity(0.1)

        qppath = QPainterPath()
        qppath.moveTo(sidebar_rect.width() * 0.2, 0)
        qppath.quadTo(sidebar_rect.width() * 0.3, sidebar_rect.height()
                      * 0.5, sidebar_rect.width() * 0.2, sidebar_rect.height() - 1)
        qppath.lineTo(0, sidebar_rect.height())
        qppath.lineTo(0, 0)
        qp.setClipPath(qppath)
        qp.drawRect(1, 1, sidebar_rect.width() - 1, sidebar.height() - 1)

        # Left border highlight
        qp.setOpacity(1.0)
        gradient = QLinearGradient(0, 0, 8, 0)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 80))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        # qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, 8, sidebar_rect.height())

        qp.end()

    def addGadget(self, gadget):
        self.gadgets.append(gadget)
        self.splitter.addWidget(self.gadgets[-1])


class Gadget(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(180, 100)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(0)
        self.layout.setContentsMargins(8, 8, 8, 8)

        self.layout.addWidget(aero.AeroButton())

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        gadget_rect = self.geometry()

        # Fill gradient
        qp.setOpacity(1.0)
        gradient = QLinearGradient(0, 0, gadget_rect.width(), 0)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 10))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, gadget_rect.width(), gadget_rect.height())

        # Slight border gradients
        qp.setOpacity(1.0)

        gradient = QLinearGradient(0, 0, 0, 4)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 80))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, gadget_rect.width(), 4)

        gradient = QLinearGradient(
            0, gadget_rect.height() - 4, 0, gadget_rect.height())
        gradient.setColorAt(0.0, QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QColor(255, 255, 255, 20))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, gadget_rect.height() - 4,
                    gadget_rect.width(), gadget_rect.height())

        # Left border highlight
        qp.setOpacity(1.0)
        gradient = QLinearGradient(0, 0, 8, 0)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 100))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, 8, gadget_rect.height())

        qp.end()


class GadgetObama(Gadget):
    def __init__(self):
        super().__init__()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setOpacity(0.4)
        qp.drawImage(0, 0, QImage('Obamahedron.gif').scaled(
            self.rect().width(), self.rect().height()))

        super().paintEvent(event)
        qp.end()


App = QApplication(sys.argv)
sidebar = Sidebar()
sys.exit(App.exec())
