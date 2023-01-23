from functools import partial
from PySide6.QtGui import QIcon
from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout,
    QSizePolicy,
    QToolButton,
)


class MainMenu(QWidget):
    def __init__(self, parent, switch_view):
        super().__init__(parent)
        main_widget_vbox = QVBoxLayout()
        main_widget_vbox.setAlignment(Qt.AlignCenter)
        self.setLayout(main_widget_vbox)
        self.switch_view = switch_view

        # Welcome label
        title = QLabel("Welcome to CheckMate, a chess tournament assistant.")
        title.setFixedHeight(50)
        title_font = title.font()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        # Buttons container
        qv_box_layout = QVBoxLayout()
        qv_box_layout.setAlignment(Qt.AlignCenter)
        qv_box_layout.setSpacing(10)

        # Buttons
        buttons_content = [
            {
                "label": "Tournaments",
                "view": "tournaments",
                "icon": "./assets/tournaments_icon.png",
            },
            {
                "label": "Players",
                "view": "players",
                "icon": "./assets/players_icon.png",
            },
            {
                "label": "Reports",
                "view": "reports",
                "icon": "./assets/reports_icon.png",
            },
        ]

        for content in buttons_content:
            button = QToolButton()
            button.setMinimumWidth(200)
            icon = QIcon(content["icon"])
            button.setIcon(icon)
            button.setText(content["label"])
            button.setToolButtonStyle(
                Qt.ToolButtonStyle.ToolButtonTextUnderIcon
            )
            font = button.font()
            font.setPointSize(20)
            button.setFont(font)
            button.setIconSize(QSize(40, 40))
            button.clicked.connect(partial(self.switch_view, content["view"]))
            qv_box_layout.addWidget(button)

        # Append widgets to layout
        main_widget_vbox.addWidget(title)
        main_widget_vbox.addLayout(qv_box_layout)
