from cli_client.service.service import API_URL


def get_players_report():
    print(f"{API_URL}/reports/players")
    input("Press a key to exit")


def get_tournaments_report():
    print(f"{API_URL}/reports/tournaments")
    input("Press a key to exit")


def get_tournament_report():
    tournament_id = input("Enter the Tournament ID: ")
    print(f"{API_URL}/reports/tournaments/{tournament_id}")
    input("Press a key to exit")
