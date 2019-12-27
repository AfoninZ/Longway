import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5.QtGui import QPainter, QPainterPath, QColor, QPen, QBrush, QLinearGradient
from PyQt5.QtCore import Qt, QPoint, QRect


class AeroButtonBase(QPushButton):
    def __init__(self):
        super(QPushButton, self).__init__()
        self.hovered = False
        self.pressed = False

        self.outline = QColor(0, 0, 0)
        self.color_text = QColor(255, 255, 255)

        self.color_outline_normal = QColor(0, 0, 0)
        self.color_border_normal = QColor(0, 0, 0)
        self.color_shadow_normal = QColor(0, 0, 0)

        self.color_outline_highlight = QColor(0, 0, 0)
        self.color_border_highlight = QColor(0, 0, 0)
        self.color_shadow_highlight = QColor(0, 0, 0)

        self.color_outline_pressed = QColor(0, 0, 0)
        self.color_border_pressed = QColor(0, 0, 0)
        self.color_shadow_pressed = QColor(0, 0, 0)

        self.opacity = 1.0
        self.roundness = 4

        self.show()

    def paintEvent(self, event):
        # Initializing QPainter
        qp = QPainter()
        qp.begin(self)
        qp.setRenderHint(QPainter.Antialiasing)
        button_rect = self.geometry()
        # Check if hovered or pressed
        color_outline = self.color_outline_normal
        color_border = self.color_border_normal
        color_shadow = self.color_shadow_normal

        if self.isEnabled():
            if self.hovered:
                color_outline = self.color_outline_highlight
                color_border = self.color_border_highlight
                color_shadow = self.color_shadow_highlight
            if self.pressed:
                color_outline = self.color_outline_pressed
                color_border = self.color_border_pressed
                color_shadow = self.color_shadow_pressed
        else:
            color_border = QColor(50, 50, 50)
            color_shadow = QColor(50, 50, 50)
        # Button outline
        qp.setPen(QPen(QBrush(color_outline), 2.0))
        outline = QPainterPath()
        outline.addRoundedRect(0, 0, button_rect.width(
        ), button_rect.height(), self.roundness, self.roundness)
        qp.setOpacity(self.opacity)
        qp.drawPath(outline)
        # Gradient
        gradient = QLinearGradient(0, 0, 0, button_rect.height())
        gradient.setColorAt(0.0, color_border)
        gradient.setColorAt(0.4, color_shadow)
        gradient.setColorAt(0.6, color_shadow)
        gradient.setColorAt(1.0, color_border)
        qp.setBrush(QBrush(gradient))
        qp.setPen(QPen(QBrush(color_border), 2.0))
        # Main button
        qppath = QPainterPath()
        qppath.addRoundedRect(1, 1, button_rect.width(
        ) - 2, button_rect.height() - 2, self.roundness, self.roundness)
        qp.setClipPath(qppath)
        qp.setOpacity(self.opacity)
        qp.drawRoundedRect(1, 1, button_rect.width(
        ) - 2, button_rect.height() - 2, self.roundness, self.roundness)
        # Glass highlight
        qp.setBrush(QBrush(Qt.white))
        qp.setPen(QPen(QBrush(Qt.white), 0.01))
        qp.setOpacity(0.30)
        qp.drawRect(1, 1, button_rect.width() - 2,
                    (button_rect.height() / 2) - 2)
        # Text
        qp.setFont(self.font())
        qp.setPen(self.color_text)
        qp.setOpacity(1.0)
        qp.drawText(QRect(0, 0, button_rect.width(), button_rect.height()), Qt.AlignCenter, self.text())
        qp.end()

    def enterEvent(self, event):
        self.hovered = True
        self.repaint()

    def leaveEvent(self, event):
        self.hovered = False
        self.repaint()

    def mousePressEvent(self, event):
        self.click()
        self.pressed = True
        self.repaint()

    def mouseReleaseEvent(self, event):
        self.pressed = False
        self.repaint()


class AeroButton(AeroButtonBase):
    def __init__(self):
        super(QPushButton, self).__init__()

        self.hovered = False
        self.pressed = False

        self.outline = QColor(74, 86, 95)
        self.color_text = QColor(20, 30, 35)

        self.color_outline_normal = QColor(74, 86, 95)
        self.color_border_normal = QColor(255, 255, 255)
        self.color_shadow_normal = QColor(182, 195, 205)

        self.color_outline_highlight = QColor(31, 87, 167)
        self.color_border_highlight = QColor(255, 255, 255)
        self.color_shadow_highlight = QColor(148, 199, 239)

        self.color_outline_pressed = QColor(31, 87, 167)
        self.color_border_pressed = QColor(164, 219, 249)
        self.color_shadow_pressed = QColor(81, 163, 212)

        self.opacity = 1.0
        self.roundness = 4


class AeroIconLabel(QWidget):
    def __init__(self):
        super().__init__()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = AeroButton()
    sys.exit(app.exec_())
