from requests import HTTPError

from cli_client.utils.input_validation import (
    validate_birthdate,
    validate_chess_id,
    validate_elo,
)
from cli_client.service.service import API_URL, fetch_data, post_data
from cli_client.utils.utils import display_data_as_table

PLAYER_ACCESSORS = [
    "id",
    "chess_id",
    "first_name",
    "last_name",
    "elo",
    "birthdate",
]


def display_players():
    players_data = get_players()
    if players_data:
        display_data_as_table(players_data, PLAYER_ACCESSORS)


def get_players():
    try:
        return fetch_data(f"{API_URL}/players")
    except HTTPError:
        print("Could not find players")
        return None


def create_player():
    while True:
        chess_id = input("Chess ID: \n")
        if not validate_chess_id(chess_id):
            print(
                "Invalid Chess ID. Must be 2 uppercase letters followed by 5 digits."
            )
            continue

        first_name = input("First name:\n")
        last_name = input("Last name: \n")

        birthdate = input("Birthdate (YYYY-MM-DD): \n")
        if not validate_birthdate(birthdate):
            print(
                "Invalid birthdate. Format must be YYYY-MM-DD and player must be at least 1 year old."
            )
            continue

        elo = input("Current ELO: \n")
        if not validate_elo(elo):
            print("Invalid ELO. Must be a positive integer.")
            continue
        break

    while True:
        player = {
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "elo": elo,
            "chess_id": chess_id,
        }

        url = f"{API_URL}/players"

        try:
            post_data(url, player)
            print("Player successfully created")
            input("Press a key to continue")
            break
        except HTTPError:
            print("Could not create player")
            choice = input("Retry?\n y/n")
            match choice:
                case "y":
                    continue
                case "n":
                    break
                case _:
                    break
