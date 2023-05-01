from flask import make_response, Response

from backend.abstract.classes.router import Router
from backend.rounds.controller import RoundController
from backend.abstract.typing.model_typing import PrimaryKey
from backend.abstract.response_codes import ResCode


class RoundRouter(Router):
    def __init__(self) -> None:
        self.controller = RoundController()

    def create_round(self, tournament_id: PrimaryKey) -> Response:
        try:
            round_id = self.controller.create_round(tournament_id)
            return make_response(
                {"message": "Round created", "payload": round_id},
                ResCode.OK.value,
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find round"},
                ResCode.BAD_REQUEST.value,
            )

    def get_round(self, round_id: PrimaryKey) -> Response:
        try:
            round = self.controller.get_round(round_id, rounds=True)
            return make_response(
                {"message": "Round found", "payload": round}, ResCode.OK.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find round"}, ResCode.BAD_REQUEST.value
            )

    def get_all_rounds(self) -> Response:
        try:
            rounds = self.controller.get_all_rounds(rounds=True)
            return make_response(
                {"message": "Round found", "payload": rounds}, ResCode.OK.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find round"}, ResCode.BAD_REQUEST.value
            )

    def update_round(self, round_id: PrimaryKey, request) -> Response:
        try:
            self.controller.update_round(round_id, request)
            return make_response(
                {"message": "Round found", "payload": round}, ResCode.OK.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find round"}, ResCode.BAD_REQUEST.value
            )

    def update_round_games(self, round_id: PrimaryKey, request) -> Response:
        try:
            self.controller.update_all_round_games(round_id, request)
            return make_response(
                {"message": f"All games for round {round_id} updated"},
                ResCode.OK.value,
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find round"},
                ResCode.BAD_REQUEST.value,
            )
