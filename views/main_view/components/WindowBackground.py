from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QLabel, QVBoxLayout


class WindowBackground(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setPixmap(QPixmap("./assets/background.png"))
        self.setScaledContents(True)
        self.setGeometry(0, 0, 1080, 720)
        self.setLayout(QVBoxLayout())
