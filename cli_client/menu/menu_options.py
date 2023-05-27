from enum import auto, Enum


class MenuOptions(Enum):
    PlayerSubMenu = auto()
    TournamentSubMenu = auto()
    ReportSubMenu = auto()
    ViewPlayers = auto()
    AddPlayer = auto()
    ViewTournaments = auto()
    AddTournament = auto()
    ViewTournament = auto()
    PlayersReport = auto()
    TournamentsReport = auto()
    TournamentReport = auto()
    Back = auto()
    Exit = auto()


players_submenu = {
    "title": "Players",
    "options": [
        ("View players", MenuOptions.ViewPlayers),
        ("Add player", MenuOptions.AddPlayer),
        ("Back", MenuOptions.Back),
    ],
}

tournaments_submenu = {
    "title": "Tournaments",
    "options": [
        ("View tournaments", MenuOptions.ViewTournaments),
        ("Add tournament", MenuOptions.AddTournament),
        ("View specific tournament", MenuOptions.ViewTournament),
        ("Back", MenuOptions.Back),
    ],
}

reports_submenu = {
    "title": "Reports",
    "options": [
        ("View players report", MenuOptions.PlayersReport),
        ("View tournaments report", MenuOptions.TournamentsReport),
        ("View detailed tournament report", MenuOptions.TournamentReport),
        ("Back", MenuOptions.Back),
    ],
}

main_menu = {
    "title": "Main menu",
    "options": [
        ("Players menu", MenuOptions.PlayerSubMenu),
        ("Tournaments menu", MenuOptions.TournamentSubMenu),
        ("Reports menu", MenuOptions.ReportSubMenu),
        ("Exit", MenuOptions.Exit),
    ],
}

submenu_map = {
    MenuOptions.PlayerSubMenu: players_submenu,
    MenuOptions.ViewPlayers: players_submenu,
    MenuOptions.AddPlayer: players_submenu,
    MenuOptions.TournamentSubMenu: tournaments_submenu,
    MenuOptions.ViewTournaments: tournaments_submenu,
    MenuOptions.AddTournament: tournaments_submenu,
    MenuOptions.ViewTournament: tournaments_submenu,
    MenuOptions.ReportSubMenu: reports_submenu,
    MenuOptions.PlayersReport: reports_submenu,
    MenuOptions.TournamentsReport: reports_submenu,
    MenuOptions.TournamentReport: reports_submenu,
    MenuOptions.Back: main_menu,
}
