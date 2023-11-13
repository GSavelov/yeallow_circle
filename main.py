import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect
from PyQt5 import uic
from random import randint


class App(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('yellow_circle.ui', self)
        self.pushButton.clicked.connect(self.circle)
        self.draw = False

    def circle(self):
        self.draw = True
        self.repaint()

    def paintEvent(self, pe):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            d = randint(1, min(self.width(), self.height()))
            rect = QRect(randint(0, self.width() - d), randint(0, self.height() - d), d, d)
            qp.setBrush(QColor('yellow'))
            qp.drawEllipse(rect)
            qp.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
