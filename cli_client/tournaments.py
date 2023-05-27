from cli_client.main import API_URL, display_data_as_table
from cli_client.services import fetch_data

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
    tournaments_data = fetch_data(f"{API_URL}/tournaments")
    display_data_as_table(tournaments_data, TOURNAMENT_ACCESSORS)


def create_tournament():
    pass
