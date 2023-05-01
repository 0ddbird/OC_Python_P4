from flask import make_response
from backend.abstract.classes.router import Router
from backend.abstract.response_codes import ResCode
from backend.reports.controller import ReportController


class ReportRouter(Router):
    def __init__(self) -> None:
        self.controller = ReportController()

    def get_reports(self):
        self.controller.get_reports()
        return make_response({"message": "Hello"}, ResCode.OK.value)

    def get_players(self):
        try:
            self.controller.get_players()
            return make_response({"message": "Hello"}, ResCode.OK.value)
        except Exception:
            return make_response(
                {"message": "bad payload"}, ResCode.BAD_REQUEST
            )

    def get_tournaments(self):
        try:
            self.controller.get_tournaments()
            return make_response({"message": "Hello"}, ResCode.OK.value)
        except Exception:
            return make_response(
                {"message": "bad payload"}, ResCode.BAD_REQUEST
            )

    def get_tournament(self, tournament_id, base, players, rounds):
        try:
            self.controller.get_tournament(
                tournament_id, base, players, rounds
            )
            return make_response({"message": "Hello"}, ResCode.OK.value)
        except Exception:
            return make_response(
                {"message": "bad payload"}, ResCode.BAD_REQUEST
            )

    def post_players(self):
        try:
            self.controller.post_players()
            return make_response({"message": "Hello"}, ResCode.OK.value)
        except Exception:
            return make_response(
                {"message": "bad payload"}, ResCode.BAD_REQUEST
            )

    def post_tournaments(self):
        try:
            self.controller.post_tournaments()
            return make_response({"message": "Hello"}, ResCode.OK.value)
        except Exception:
            return make_response(
                {"message": "bad payload"}, ResCode.BAD_REQUEST
            )

    def post_tournament(self, tournament_id, base, players, rounds):
        try:
            self.controller.post_tournament(
                tournament_id, base, players, rounds
            )
            return make_response({"message": "Hello"}, ResCode.OK.value)
        except Exception:
            return make_response(
                {"message": "bad payload"}, ResCode.BAD_REQUEST
            )
