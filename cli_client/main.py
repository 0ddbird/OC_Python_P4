from enum import Enum

import click
from rich.table import Table
from rich.console import Console

from cli_client.services import fetch_data
from cli_client.utils.utils import snake_to_title

API_URL = "http://localhost:5000"


class Menu(Enum):
    PlayerSubMenu = "1"
    TournamentSubMenu = "2"
    ReportSubMenu = "3"
    ViewPlayers = "4"
    AddPlayer = "5"
    ViewTournaments = "6"
    AddTournaments = "7"
    ViewTournament = "8"
    ViewPlayersReport = "9"
    ViewTournamentsReport = "10"
    ViewTournamentReport = "11"


def display_data_as_table(data, column_names):
    console = Console()
    table = Table(show_header=True, header_style="bold yellow")

    for column_name in column_names:
        table.add_column(
            snake_to_title(column_name)
        )  # Convert the column name to Title Case

    for item in data:
        try:
            table.add_row(*(str(item.get(name)) for name in column_names))
        except TypeError:
            print(f"Missing data in item: {item}")

    console.print(table)


def user_prompt(answers):
    choice = None
    while choice not in answers:
        choice = input()


def prompt_report_type():
    while True:
        print(
            "\nChoose the report type:\n"
            "1. Player Report\n"
            "2. Tournaments Report\n"
            "3. Specific Tournament Report\n"
            "4. Exit\n"
        )

        user_choice = input("Enter your choice: ")

        if user_choice == "1":
            return f"{API_URL}/reports/players"
        elif user_choice == "2":
            return f"{API_URL}/reports/tournaments"
        elif user_choice == "3":
            tournament_id = input("Enter the Tournament ID: ")
            return f"{API_URL}/reports/tournaments/{tournament_id}"
        elif user_choice == "4":
            exit(0)
        else:
            print("\nInvalid option. Please try again.")


def main():
    report_url = prompt_report_type()
    click.secho(report_url, fg="blue", underline=True)
    print(report_url)
    input("Press a key to exit")


if __name__ == "__main__":
    main()
