from flask import make_response, Request, Response

from backend.abstract.classes.Router import Router
from backend.players.PlayerController import PlayerController
from backend.abstract.exceptions.dao_exceptions import PlayerCreationException
from backend.abstract.typing.model_typing import PrimaryKey
from backend.abstract.response_codes import ResCode


class PlayerRouter(Router):
    def __init__(self) -> None:
        self.controller = PlayerController()

    def handle_get_players(self) -> Response:
        players = self.controller.get_all_players()
        return make_response(
            {
                "message": "Successfully fetched players",
                "payload": players,
            },
            ResCode.OK.value,
        )

    def handle_post_player(self, http_request: Request) -> Response:
        player = {
            "chess_id": http_request.json.get("chess_id"),
            "first_name": http_request.json.get("first_name"),
            "last_name": http_request.json.get("last_name"),
            "birthdate": http_request.json.get("birthdate"),
            "elo": http_request.json.get("elo"),
        }
        try:
            player_id = self.controller.create_player(player)
            return make_response(
                {
                    "message": "Successfully created player",
                    "payload": player_id,
                },
                ResCode.CREATED.value,
            )
        except PlayerCreationException as e:
            return make_response(
                {
                    "message": "Error while creating player",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_player(self, player_id) -> Response:
        player = self.controller.get_player(player_id)
        return make_response(
            {
                "message": "Successfully fetched player",
                "payload": player,
            },
            ResCode.OK.value,
        )

    def handle_update_player(self, id, http_request: Request) -> Response:
        player_data = {
            "id": id,
            "chess_id": http_request.json.get("chess_id"),
            "first_name": http_request.json.get("first_name"),
            "last_name": http_request.json.get("last_name"),
            "birthdate": http_request.json.get("birthdate"),
            "elo": http_request.json.get("elo"),
        }
        try:
            self.controller.update_player(player_data)
            return make_response(
                {
                    "message": "Successfully updated player",
                },
                ResCode.OK.value,
            )

        except Exception as e:
            return make_response(
                {"message": "Error while updating player", "error": str(e)},
                ResCode.BAD_REQUEST.value,
            )

    def handle_delete_player(self, player_id: PrimaryKey) -> Response:
        try:
            self.controller.delete_player(int(player_id))
            return make_response(
                {
                    "message": "Successfully deleted player",
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {"message": "Error while deleting player", "error": str(e)},
                ResCode.BAD_REQUEST.value,
            )
