from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QMainWindow

from controllers.Controller import Controller
from views.main_view.components.MainMenu import MainMenu
from views.main_view.components.WindowBackground import WindowBackground
from views.players.Players import Players
from views.reports.Reports import Reports
from views.tournaments.Tournaments import Tournaments


class MainView(QMainWindow):
    def __init__(self, controller: Controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("CheckMate")
        self.setWindowIcon(QIcon("./assets/icon.png"))
        self.resize(1080, 720)

        self.container = WindowBackground()
        self.current_view = MainMenu(self, self.switch_view)
        self.container.layout().addWidget(self.current_view)
        self.setCentralWidget(self.container)

        self.views = {
            "tournaments": Tournaments,
            "players": Players,
            "reports": Reports,
        }

    def switch_view(self, view_name):
        new_view = self.views.get(view_name)(self, self.controller)
        print(self.views.get(view_name))
        self.container.layout().removeWidget(self.current_view)
        self.current_view.deleteLater()
        self.container.layout().addWidget(new_view)
        self.current_view = new_view
