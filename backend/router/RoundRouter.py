from flask import make_response, Response

from backend.controllers.RoundController import RoundController
from backend.models.model_typing import PrimaryKey
from backend.router.response_codes import ResCode


class RoundRouter:
    def __init__(self) -> None:
        self.controller = RoundController()

    def handle_create_round(self, tournament_id: PrimaryKey) -> Response:
        try:
            round_id = self.controller.create_round(tournament_id)
            return make_response(
                {
                    "message": "Round created",
                    "payload": round_id,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find round",
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_round(self, round_id: PrimaryKey) -> Response:
        try:
            round = self.controller.get_round(round_id)
            return make_response(
                {
                    "message": "Round found",
                    "payload": round,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find round",
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_update_round(self, round_id: PrimaryKey, request) -> Response:
        try:
            self.controller.update_round(round_id, request)
            return make_response(
                {
                    "message": "Round found",
                    "payload": round,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find round",
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )
