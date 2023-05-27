from cli_client.main import API_URL, display_data_as_table
from cli_client.services import fetch_data

PLAYER_ACCESSORS = ["id", "chess_id", "first_name", "last_name", "elo", "birthdate"]


def get_players():
    players_data = fetch_data(f"{API_URL}/players")
    display_data_as_table(players_data, PLAYER_ACCESSORS)


def create_player():
    pass
