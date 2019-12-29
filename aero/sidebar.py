from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QLabel, QStyle
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen, QBrush, QLinearGradient, QImage, QIcon, QPixmap
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

        # Splitter for storing tiles
        self.tiles = []

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
        self.addTile(TileSlideshow())
        self.addTile(TileTest())
        self.addTile(Tile())
        self.addTile(Tile())
        self.addTile(QWidget())
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
        gradient = QLinearGradient(0, 0, 2, 0)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 80))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        # qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, 8, sidebar_rect.height())

        qp.end()

    def addTile(self, tile):
        self.tiles.append(tile)
        self.splitter.addWidget(self.tiles[-1])


class Tile(QWidget):
    def __init__(self):
        super().__init__()
        self.name = 'Tile'

        self.resize(180, 50)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.layout = QVBoxLayout(self)
        self.layout.setSpacing(4)
        self.layout.setContentsMargins(8, 8, 8, 8)

        self.painted = []
        '''for i in range(5):
            button = aero.ButtonInvisible()
            button.setText(f'Button #{i}')
            button.setIcon(self.style().standardIcon(getattr(QStyle, 'SP_FileIcon')))
            self.layout.addWidget(button)'''

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        tile_rect = self.geometry()

        # Fill gradient
        qp.setOpacity(1.0)
        gradient = QLinearGradient(0, 0, tile_rect.width(), 0)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 10))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, tile_rect.width(), tile_rect.height())

        # Slight border gradients
        qp.setOpacity(1.0)

        gradient = QLinearGradient(0, 0, 0, 4)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 80))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, tile_rect.width(), 4)

        gradient = QLinearGradient(
            0, tile_rect.height() - 4, 0, tile_rect.height())
        gradient.setColorAt(0.0, QColor(0, 0, 0, 0))
        gradient.setColorAt(1.0, QColor(255, 255, 255, 20))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, tile_rect.height() - 4,
                    tile_rect.width(), tile_rect.height())

        # Left border highlight
        qp.setOpacity(1.0)
        gradient = QLinearGradient(0, 0, 8, 0)
        gradient.setColorAt(0.0, QColor(255, 255, 255, 100))
        gradient.setColorAt(1.0, QColor(0, 0, 0, 0))

        qp.setBrush(QBrush(gradient))
        qp.setPen(Qt.transparent)
        qp.drawRect(0, 0, 8, tile_rect.height())

        for i in self.painted:
            i.paintEvent(event)

        qp.end()


class TileTest(Tile):
    def __init__(self):
        super().__init__()
        self.name = 'Test Tile'

        self.layout.addStretch()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)

        qp.setOpacity(0.4)
        qp.drawImage(0, 0, QImage('documents.png').scaled(
            self.rect().width(), self.rect().height()))

        super().paintEvent(event)
        qp.end()


class TileSlideshow(Tile):
    def __init__(self):
        super().__init__()
        self.name = 'Slide Show'

        self.imageList = ['2WbxngR3LEg.jpg', 'danir.png', 'memech.png', 'nasral.png', 'test.png']
        self.imageIndex = 1
        self.pixmap = QPixmap('slides/' + self.imageList[self.imageIndex]).scaledToWidth(180 - 8 - 8)

        self.image = QLabel()
        self.image.setPixmap(self.pixmap)

        self.buttonPrev = aero.ButtonInvisible()
        self.buttonPrev.setText('Back')
        self.buttonPrev.clicked.connect(self.showPrev)

        self.buttonNext = aero.ButtonInvisible()
        self.buttonNext.setText('Next')
        self.buttonNext.clicked.connect(self.showNext)

        self.button = aero.ButtonInvisible()
        self.button.setText(self.name)
        self.layout.addWidget(self.button)
        self.layout.addWidget(self.image)

        self.layout.setAlignment(self.button, Qt.AlignTop)

        self.buttons = QHBoxLayout()
        self.buttons.setSpacing(4)
        self.buttons.setContentsMargins(0, 0, 0, 0)

        self.buttons.addWidget(self.buttonPrev)
        self.buttons.addWidget(self.buttonNext)

        self.layout.addLayout(self.buttons)

    def showPrev(self):
        self.imageIndex -= 1
        if self.imageIndex < 0:
            self.imageIndex = len(self.imageList) - 1
        self.updatePixmap()

    def showNext(self):
        self.imageIndex += 1
        if self.imageIndex > len(self.imageList) - 1:
            self.imageIndex = 0
        self.updatePixmap()

    def updatePixmap(self):
        self.pixmap = QPixmap('slides/' + self.imageList[self.imageIndex]).scaledToWidth(180 - 8 - 8)
        self.image.setPixmap(self.pixmap)


App = QApplication(sys.argv)
sidebar = Sidebar()
sys.exit(App.exec())
