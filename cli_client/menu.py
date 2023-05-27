from enum import Enum
from click import secho

from cli_client.main import API_URL
from cli_client.players import create_player, get_players
from cli_client.tournaments import create_tournament, get_tournaments


class MainMenuChoice(Enum):
    Players = "1"
    Tournaments = "2"
    Reports = "3"
    Exit = "4"


class ReportsMenuChoice(Enum):
    Players = "1"
    Tournaments = "2"
    Tournament = "3"
    Main = "4"


class TournamentMenuChoice(Enum):
    Read = "1"
    Create = "2"
    Main = "3"


class PlayerMenuChoice(Enum):
    Read = "1"
    Create = "2"
    Main = "3"


class MainMenu:
    name = "Main menu"
    choices = MainMenuChoice
    options = (
        ("1. Players", MainMenuChoice.Players, players_menu()),
        ("2. Tournaments", MainMenuChoice.Tournaments, tournaments_menu())(
            "3. Reports", MainMenuChoice.Reports, reports_menu()
        ),
    )


class PlayerMenu:
    name = "Players"
    choices = PlayerMenuChoice
    options = (
        ("1. View players", PlayerMenuChoice.Read, get_players()),
        ("2. Add new player", PlayerMenuChoice.Create, create_player()),
        ("3. Back to main menu", PlayerMenuChoice.Main),
    )


class Menu:
    @staticmethod
    def default(choice: str):
        secho(f"Invalid choice: {choice}", fg="red")

    @staticmethod
    def is_valid_choice(choice, choice_enum):
        return choice in [e.value for e in choice_enum]

    def main_menu(self) -> None:
        secho("CheckMate - Your chess tournament assistant")

        while True:
            secho("1. Players\n" "2. Tournaments\n" "3. Reports\n" "4. Exit\n")

            choice = input("Please select a category. (1-4)")

            if not self.is_valid_choice(choice, MainMenuChoice):
                secho("Please type a number in the given range")
                continue

            match choice:
                case MainMenuChoice.Players:
                    self.players_menu()
                case MainMenuChoice.Tournaments:
                    self.tournaments_menu()
                case MainMenuChoice.Reports:
                    self.reports_menu()
                case MainMenuChoice.Exit:
                    exit(0)
                case _:
                    self.default(choice)

    def players_menu(self) -> None:
        secho("Players")
        while True:
            secho("1. View players\n" "2. Add player\n" "3. Back to main menu\n")
            choice = input("Please select a category. (1-3)")

            if not self.is_valid_choice(choice, PlayerMenuChoice):
                secho("Please type a number in the given range")
                continue

            match choice:
                case PlayerMenuChoice.Read:
                    get_players()
                case PlayerMenuChoice.Create:
                    create_player()
                case PlayerMenuChoice.Main:
                    self.menu()
                case _:
                    self.default(choice)

    def tournaments_menu(self) -> None:
        secho("Tournaments")
        while True:
            secho(
                "1. View tournaments\n"
                "2. Create tournament\n"
                "3. Back to main menu\n"
            )
            choice = input("Please select a category. (1-3)")

            if not self.is_valid_choice(choice, TournamentMenuChoice):
                secho("Please type a number in the given range")
                continue

            match choice:
                case TournamentMenuChoice.Read:
                    get_tournaments()
                case TournamentMenuChoice.Create:
                    create_tournament()
                case TournamentMenuChoice.Main:
                    self.menu()
                case _:
                    self.default(choice)

    def reports_menu(self) -> None:
        secho("Reports")
        while True:
            secho(
                "1. All players\n"
                "2. All tournaments\n"
                "3. Single tournament\n"
                "4. Back to main menu\n"
            )
            choice = input("Please select a category. (1-4)")

            if not self.is_valid_choice(choice, ReportsMenuChoice):
                secho("Please type a number in the given range")
                continue

            match choice:
                case ReportsMenuChoice.Players:
                    secho(f"{API_URL}/reports/players", fg="blue", underline=True)
                case ReportsMenuChoice.Tournaments:
                    secho(f"{API_URL}/reports/tournaments", fg="blue", underline=True)
                case ReportsMenuChoice.Tournament:
                    tournament_id = input("Enter the Tournament ID: ")
                    secho(f"{API_URL}/reports/tournaments/{tournament_id}")
                case ReportsMenuChoice.Main:
                    self.menu()
                case _:
                    self.default(choice)
