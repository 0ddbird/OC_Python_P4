from urllib.parse import urlencode
from service.service import API_URL
from utils.utils import user_ok


def get_players_report():
    print(f"{API_URL}/reports/players")
    input("Press a key to exit")


def get_tournaments_report():
    print(f"{API_URL}/reports/tournaments")
    input("Press a key to exit")


def get_tournament_report():
    tournament_id = input("Enter the Tournament ID: ")
    params = {}
    if user_ok("Do you want to include the players?"):
        params["players"] = "true"
    if user_ok("Do you want to include the rounds?"):
        params["rounds"] = "true"

    param_string = urlencode(params)
    url = f"{API_URL}/reports/tournaments/{tournament_id}"
    if param_string:
        url += f"?{param_string}"
    print(url)
    input("Press a key to exit")
