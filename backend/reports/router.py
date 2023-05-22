from flask import render_template, abort
from backend.abstract.classes.router import Router
from backend.reports.controller import ReportController


class ReportRouter(Router):
    def __init__(self) -> None:
        self.controller = ReportController()

    def get_players(self):
        players = self.controller.get_players()
        return render_template("players.html", players=players)

    def get_tournaments(self):
        tournaments = self.controller.get_tournaments()
        return render_template("tournaments.html", tournaments=tournaments)

    def get_tournament(self, tournament_id, players=False, rounds=False):
        try:
            tournament = self.controller.get_tournament(
                tournament_id=tournament_id, players=players, rounds=rounds
            )
            return render_template("tournament.html", tournament=tournament)
        except Exception:
            abort(404)
