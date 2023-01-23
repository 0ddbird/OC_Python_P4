from datetime import datetime

from PySide6.QtCore import QDate
from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QDateEdit,
)

from controllers.PlayerController import PlayerController


class NewPlayerForm(QWidget):
    def __init__(self, player_controller: PlayerController, hide_form):
        super().__init__()
        self.setWindowTitle("Create player")
        self.player_controller = player_controller
        self.hide_form = hide_form

        layout = QFormLayout()
        self.p_id = QLineEdit()
        self.first_name = QLineEdit()
        self.last_name = QLineEdit()
        self.birthdate = QDateEdit()
        self.birthdate.setCalendarPopup(True)
        self.elo = QLineEdit()
        layout.addRow("National Chess ID", self.p_id)
        layout.addRow("First Name:", self.first_name)
        layout.addRow("Last Name:", self.last_name)
        layout.addRow("Birthdate:", self.birthdate)
        layout.addRow("ELO:", self.elo)

        self.submit_button = QPushButton("Submit")
        self.submit_button.clicked.connect(self.submit)
        layout.addRow(self.submit_button)

        self.cancel_button = QPushButton("Cancel")
        self.cancel_button.clicked.connect(self.cancel)
        layout.addRow(self.cancel_button)

        self.setLayout(layout)

    @staticmethod
    def qdate_to_datetime(qdate: QDate):
        return datetime.fromordinal(qdate.toPython().toordinal())

    def submit(self):
        p_id = self.p_id.text()
        first_name = self.first_name.text()
        last_name = self.last_name.text()
        birthdate = self.qdate_to_datetime(self.birthdate.date())
        elo = int(self.elo.text())
        self.player_controller.create_player(
            p_id, first_name, last_name, birthdate, elo
        )
        self.hide_form()

    def cancel(self):
        self.p_id.clear()
        self.first_name.clear()
        self.last_name.clear()
        self.birthdate.clear()
        self.elo.clear()
        self.hide_form()
