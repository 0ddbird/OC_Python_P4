from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
)


class Reports(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        widget = QVBoxLayout()
        widget.setAlignment(Qt.AlignCenter)
        self.setLayout(widget)
        self.controller = controller

        # Welcome label
        title = QLabel("Reports")
        title.setFixedHeight(50)
        title_font = title.font()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Append widgets to layout
        widget.addWidget(title)
