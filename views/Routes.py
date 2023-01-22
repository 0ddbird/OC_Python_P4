from enum import Enum

from views.players.Players import Players
from views.reports.Reports import Reports
from views.tournaments.Tournaments import Tournaments


class Routes(Enum):
    Tournaments = Tournaments
    Players = Players
    Reports = Reports
