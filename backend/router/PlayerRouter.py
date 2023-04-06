from flask import make_response

from backend.controllers.PlayerController import PlayerController
from backend.exceptions.dao import PlayerCreationException
from backend.router.response_codes import ResCode


class PlayerRouter:
    def __init__(self):
        self.controller = PlayerController()

    def handle_get_players(self):
        players = self.controller.get_all_players()
        return make_response(
            {"message": "Successfully fetched players", "payload": players},
            ResCode.OK.value,
        )

    def handle_post_player(self, http_request):
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
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_player(self, player_id):
        player = self.controller.get_player(player_id)
        return make_response(
            {"message": "Successfully fetched player", "payload": player},
            ResCode.OK.value,
        )

    def handle_update_player(self, id, http_request):
        player_data = {
            "id": id,
            "chess_id": http_request.json.get("chess_id"),
            "first_name": http_request.json.get("first_name"),
            "last_name": http_request.json.get("last_name"),
            "birthdate": http_request.json.get("birthdate"),
            "elo": http_request.json.get("elo"),
        }
        try:
            updated_player_id = self.controller.update_player(player_data)
            return make_response(
                {
                    "message": "Successfully updated player",
                    "payload": updated_player_id,
                },
                ResCode.OK.value,
            )

        except Exception as e:
            return make_response(
                {
                    "message": "Error while updating player",
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_delete_player(self, player_id):
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
                {
                    "message": "Error while deleting player",
                },
                ResCode.BAD_REQUEST.value,
            )
