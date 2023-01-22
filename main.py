import sys
from PySide6.QtWidgets import QApplication
from controllers.Controller import Controller
from views.main_view.MainView import MainView


class App:
    def __init__(self, controller: Controller, view: MainView):
        self.controller = controller
        self.view = view

    def run(self):
        self.view.show()


def main():
    app = QApplication(sys.argv)
    controller = Controller()
    view = MainView(controller)
    main_app = App(controller, view)
    main_app.run()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
