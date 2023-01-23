from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QSizePolicy,
    QPushButton,
)

from views.players.components.NewPlayerForm import NewPlayerForm
from views.players.components.PlayersTable import PlayersTable


class Players(QWidget):
    def __init__(self, parent, controller):
        super().__init__(parent)
        self.controller = controller
        self.players = controller.player_controller.get_players()
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)
        self.setLayout(layout)
        self.layout = layout

        title = QLabel("Players")
        title.setFixedHeight(50)
        title_font = title.font()
        title_font.setPointSize(20)
        title.setFont(title_font)
        title.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)

        self.show_form_button = QPushButton("Create player")
        self.show_form_button.clicked.connect(self.show_form)
        self.new_player_form = NewPlayerForm(
            self.controller.player_controller, self.hide_form
        )
        self.new_player_form.hide()
        layout.addWidget(title)
        if self.players:
            self.table = PlayersTable(self.players)
            layout.addWidget(self.table)
        layout.addWidget(self.show_form_button)
        layout.addWidget(self.new_player_form)

    def show_form(self):
        self.new_player_form.show()
        self.show_form_button.hide()

    def hide_form(self):
        self.new_player_form.hide()
        self.show_form_button.show()
