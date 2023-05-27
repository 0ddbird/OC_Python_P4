from requests import HTTPError

from cli_client.handlers.players import get_players
from cli_client.service.service import API_URL, fetch_data, post_data
from cli_client.utils.utils import display_data_as_table

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
        tournaments_data = fetch_data(f"{API_URL}/tournaments")
        display_data_as_table(tournaments_data, TOURNAMENT_ACCESSORS)
    except HTTPError:
        print("Could not find tournaments")


def get_tournament():
    tournament_id = input(
        "Please type the ID of the tournament you want to see\n"
    )
    try:
        tournament = fetch_data(f"{API_URL}/tournaments/{tournament_id}")
        print(tournament)
        id = tournament["id"]
        name = tournament["name"]
        description = tournament["description"]
        location = tournament["location"]
        start_datetime = tournament["start_datetime"]
        end_datetime = tournament["end_datetime"]
        status = tournament["status"]

        print(
            "_____________________\n"
            "Tournament details\n"
            f"id: {id}\n"
            f"Name: {name}\n"
            f"Description: {description}\n"
            f"Location: {location}\n"
            f"Status: {status}\n"
            f"Start date: {start_datetime}\n"
            f"End date: {end_datetime}\n"
            "_____________________\n"
        )

    except HTTPError:
        print("Could not find tournament")


def create_tournament():
    while True:

        players = get_players()

        if players:
            print("Select players for the tournament:")
            for i, player in enumerate(players, start=1):
                print(f"{i}. {player['first_name']} {player['last_name']}")
            selected_player_ids = input(
                "Type the numbers of the players you want to select, separated by comma:\n"
            )
            selected_player_ids = [
                players[int(index) - 1]['id']
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

        url = f"{API_URL}/tournaments"

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
