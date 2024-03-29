from menu.menu_options import MenuOptions, main_menu, submenu_map
from handlers.players import create_player, display_players
from handlers.reports import (
    get_players_report,
    get_tournament_report,
    get_tournaments_report,
)
from handlers.tournaments import (
    create_tournament,
    get_tournament,
    get_tournaments,
)


def display_menu(menu):
    while True:
        title = menu["title"]
        options = menu["options"]
        print(title)

        for i, option in enumerate(options):
            print(f"{i+1}. {option[0]}")

        user_input = input(
            "Please type the number of the option you want to " "select\n"
        )

        try:
            user_choice = int(user_input)
            if user_choice < 1 or user_choice > len(options):
                raise ValueError("Invalid choice")
            return options[user_choice - 1][1]
        except ValueError:
            print(
                "Please select an option by typing a number between"
                f"1 and {len(options)}"
            )
            continue


def handle_user_selection(user_selection):
    match user_selection:
        case MenuOptions.PlayerSubMenu:
            pass
        case MenuOptions.TournamentSubMenu:
            pass
        case MenuOptions.ReportSubMenu:
            pass
        case MenuOptions.Back:
            pass
        case MenuOptions.ViewPlayers:
            display_players()
        case MenuOptions.AddPlayer:
            create_player()
        case MenuOptions.ViewTournaments:
            get_tournaments()
        case MenuOptions.AddTournament:
            create_tournament()
        case MenuOptions.ViewTournament:
            get_tournament()
        case MenuOptions.PlayersReport:
            get_players_report()
        case MenuOptions.TournamentsReport:
            get_tournaments_report()
        case MenuOptions.TournamentReport:
            get_tournament_report()
        case MenuOptions.Exit:
            return None
        case _:
            pass

    return submenu_map.get(user_selection, main_menu)
