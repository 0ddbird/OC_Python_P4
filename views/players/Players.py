from PySide6.QtCore import Qt
from PySide6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy

from views.players.components.PlayersTable import PlayersTable


class Players(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.players = controller.player_controller.get_players()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)

        # Welcome label
        title = QLabel("players")
        title.setFixedHeight(50)
        title_font = title.font()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        table = PlayersTable(self.players)
        # Append layouts to layout
        layout.addWidget(title)
        layout.addWidget(table)
