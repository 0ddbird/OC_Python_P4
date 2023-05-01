from flask import make_response, Request, Response

from backend.abstract.classes.router import Router
from backend.players.controller import PlayerController
from backend.abstract.exceptions.dao_exceptions import PlayerCreationException
from backend.abstract.typing.model_typing import PrimaryKey
from backend.abstract.response_codes import ResCode


class PlayerRouter(Router):
    def __init__(self) -> None:
        self.controller = PlayerController()

    def create_player(self, request: Request) -> Response:
        keys = ["chess_id", "first_name", "last_name", "birthdate", "elo"]
        player = {key: request.json.get(key) for key in keys}
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
            print(str(e))
            return make_response(
                {"message": "Error while creating player"},
                ResCode.BAD_REQUEST.value,
            )

    def get_player(self, player_id: PrimaryKey) -> Response:
        player = self.controller.get_player(player_id)
        return make_response(
            {"message": "Successfully fetched player", "payload": player},
            ResCode.OK.value,
        )

    def get_players(self) -> Response:
        players = self.controller.get_all_players()
        return make_response(
            {"message": "Successfully fetched players", "payload": players},
            ResCode.OK.value,
        )

    def update_player(self, id, request: Request) -> Response:
        keys = ["chess_id", "first_name", "last_name", "birthdate", "elo"]
        player = {key: request.json.get(key) for key in keys}
        player["id"] = id
        try:
            self.controller.update_player(player)
            return make_response(
                {"message": "Successfully updated player"},
                ResCode.OK.value,
            )

        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Error while updating player"},
                ResCode.BAD_REQUEST.value,
            )

    def delete_player(self, player_id: PrimaryKey) -> Response:
        try:
            self.controller.delete(int(player_id))
            return make_response(
                {"message": "Successfully deleted player"},
                ResCode.OK.value,
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Error while deleting player"},
                ResCode.BAD_REQUEST.value,
            )
