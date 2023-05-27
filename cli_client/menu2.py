from typing import Optional
from click import secho


class Menu:
    def __init__(self, views: dict[MainMenuChoice, View]):
        self.views = views
        self.view: Optional[View] = None

    def run(self):
        print(
            "CheckMate - Your chess tournament assistant\n"
            "1. Players\n"
            "2. Tournaments\n"
            "3. Reports\n"
            "4. Exit\n"
        )
        while True:
            choice = input("Please select a category. (1-4)")

            if not self.is_valid_choice(choice, MainMenuChoice):
                secho("Please type a number in the given range", fg="red")
                continue

            if choice == MainMenuChoice.Exit.value:
                break

            self.view = self.views[MainMenuChoice(choice)]
            self.display_menu()

    @staticmethod
    def is_valid_choice(choice, choice_enum):
        return choice in [e.value for e in choice_enum]

    def display_menu(self) -> None:
        self.view.display_header()
        while True:
            self.view.display_options()

            choice = input(
                f"Please select an option. (1-{len(self.view.options)})")

            if not self.is_valid_choice(choice, self.view.options):
                secho("Please type a number in the given range")
                continue

            selected_option = next(
                filter(lambda option: option.value.value == choice,
                       self.view.options)
            )
            selected_option.render()
