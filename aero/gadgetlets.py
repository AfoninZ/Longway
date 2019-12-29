from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QSplitter, QLabel
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen, QBrush, QLinearGradient, QImage
from PyQt5.QtCore import *
import sys

import aero


'''class IconLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QHBoxLayout()
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(0, 0, 0, 0)

        icon '''


class LetImage(QWidget):
    def __init__(self):
        super().__init__()
        self.image = 'documents.png'

    def setImage(self, image):
        self.image = image
        self.repaint()

    def paintEvent(self, event):
        qp = QPainter(self)

        qp.setOpacity(1.0)
        qp.drawImage(0, 0, QImage('./' + self.image).scaled(
            self.rect().width(), self.rect().height()))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = LetImage()
    sys.exit(app.exec_())