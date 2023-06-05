from requests import HTTPError
from rich.console import Console
from rich.table import Table
from handlers.players import get_players
from service.service import (
    API_URL,
    get_data,
    patch_data,
    post_data,
)
from utils.utils import display_data_as_table, user_ok

TOURNAMENT_ACCESSORS = [
    "id",
    "name",
    "start_datetime",
    "location",
    "current_round",
    "max_rounds",
    "status",
]


def get_tournaments():
    try:
        tournaments_data = get_data(f"{API_URL}/api/tournaments")
        display_data_as_table(tournaments_data, TOURNAMENT_ACCESSORS)
    except HTTPError:
        print("Could not find tournaments")


def get_tournament():
    id = input("Please type the ID of the tournament you want to see\n")
    try:
        tournament = get_data(f"{API_URL}/api/tournaments/{id}")
        tournament_view(tournament)
        status = tournament["status"]
        is_to_start = status == "TO_START"
        has_open_round = status == "ROUND_OPEN"
        is_started = status == "STARTED"

        if is_to_start and user_ok("Start the tournament?\n"):
            start_tournament(id)
        if is_started and user_ok("Start the round?"):
            start_tournament(id)
        if has_open_round and user_ok("Resume the tournament?"):
            resume_tournament(id)

    except HTTPError:
        print("Could not find tournament")


def resume_tournament(tournament_id):
    try:
        tournament = get_data(
            f"{API_URL}/api/tournaments/"
            f"{tournament_id}?players=true&rounds=true"
        )
        rounds = tournament.get("rounds", None)
        if not rounds:
            print("This tournament has no rounds")
        players = tournament.get("players", None)
        players_dict = {
            player["id"]: f"{player['first_name']} {player['last_name']}"
            for player in players
        }
        current_round = rounds[-1]

        for game in current_round.get("games", []):
            game_status = game.get("status", None)
            if game_status == "OPEN":
                print(
                    f"Game {game['id']} between\n"
                    f"1. {players_dict[game['p1_id']]}\nand\n"
                    f"2. {players_dict[game['p2_id']]}"
                )
                update_game(game["id"])
    except HTTPError:
        print("Could not resume tournament")


def update_game(game_id):
    while True:
        try:
            p1_score = input(
                "Enter score for Player 1 (WIN = 1, LOSE = 0, TIE = 0.5):"
            )
            p2_score = input(
                "Enter score for Player 2 (WIN = 1, LOSE = 0, TIE = 0.5):"
            )

            # Convert input strings to float
            p1_score = float(p1_score)
            p2_score = float(p2_score)

            patch_data(
                f"{API_URL}/api/games/{game_id}",
                payload={"p1_score": p1_score, "p2_score": p2_score},
            )
            print(f"Successfully updated game {game_id}")
            break
        except HTTPError as http_err:
            print(f"Error while updating game: {http_err}")
            choice = input("Retry?\n y/n")
            if choice.lower() == "n":
                break
        except ValueError:
            print(
                "Invalid input. Please enter a valid number"
                "(1.0, 0.0, or 0.5)."
            )
            choice = input("Retry?\n y/n")
            if choice.lower() == "n":
                break


def tournament_view(tournament):
    id = tournament.get("id")
    name = tournament.get("name")
    description = tournament.get("description")
    location = tournament.get("location")
    start_datetime = tournament.get("start_datetime")
    end_datetime = tournament.get("end_datetime", None)
    status = tournament.get("status")
    current_round = tournament.get("current_round")
    max_rounds = tournament.get("max_rounds")
    if end_datetime is None:
        end_datetime = "N/A"

    console = Console()

    table = Table(show_header=True, header_style="bold blue")
    table.add_column("Attribute")
    table.add_column("Value")

    table.add_row("ID", str(id))
    table.add_row("Name", name)
    table.add_row("Description", description)
    table.add_row("Location", location)
    table.add_row("Status", status)
    table.add_row("Rounds", f"{current_round} / {max_rounds}")
    table.add_row("Start Date", start_datetime)
    table.add_row("End Date", end_datetime)

    console.print(table)
    input("Press a key to continue")


def start_tournament(tournament_id):
    try:
        post_data(f"{API_URL}/api/tournaments/{tournament_id}")
        print("Tournament successfully started")
        tournament = get_data(f"{API_URL}/api/tournaments/{tournament_id}")
        tournament_view(tournament)
    except HTTPError:
        print("Could not start tournament")


def create_tournament():
    while True:
        players = get_players()

        if players:
            print("Select players for the tournament:")
            for i, player in enumerate(players, start=1):
                print(f"{i}. {player['first_name']} {player['last_name']}")
            selected_player_ids = input(
                "Type the numbers of the players you want to "
                "select, separated by comma:\n"
            )
            selected_player_ids = [
                players[int(index) - 1]["id"]
                for index in selected_player_ids.split(",")
            ]
        else:
            print("No players available.")
            return

        name = input("Tournament Name: \n")
        location = input("Tournament Location: \n")
        max_rounds = input("Number of Rounds: \n")
        description = input("Description: \n")

        tournament = {
            "name": name,
            "location": location,
            "max_rounds": max_rounds,
            "description": description,
            "players_ids": selected_player_ids,
        }

        url = f"{API_URL}/api/tournaments"

        try:
            post_data(url, tournament)
            print("Tournament successfully created")
            input("Press a key to continue")
            break
        except HTTPError:
            print("Could not create tournament")
            choice = input("Retry?\n y/n")
            match choice:
                case "y":
                    continue
                case "n":
                    break
                case _:
                    break
