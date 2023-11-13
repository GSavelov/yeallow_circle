import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRect

from ui import Ui_Form


class App(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            qp.setBrush(QColor(randint(0, 0xffffff)))
            qp.drawEllipse(rect)
            qp.end()
            self.draw = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = App()
    window.show()
    sys.exit(app.exec())
