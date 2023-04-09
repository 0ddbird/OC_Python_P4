from flask import make_response, Response
from backend.abstract.classes.Router import Router
from backend.abstract.response_codes import ResCode
from backend.games.GameController import GameController


class GameRouter(Router):
    def __init__(self):
        self.controller = GameController()

    def handle_get_game(self, game_id) -> Response:
        try:
            game = self.controller.get_game(game_id)
            return make_response(
                {
                    "message": "Game found",
                    "payload": game,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find game",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_all_games(self):
        try:
            games = self.controller.get_all_games()
            return make_response(
                {
                    "message": "Games found",
                    "payload": games,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find games",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_update_game(self, game_id, request) -> Response:
        try:
            self.controller.update_game(game_id, request)
            return make_response(
                {
                    "message": "Game updated",
                },
                ResCode.NO_CONTENT.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find game",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_games_by_id(self, request) -> Response:
        try:
            games_ids = request.json.get("games_ids")
            games = self.controller.get_games_by_id(games_ids)
            return make_response(
                {
                    "message": "Games found",
                    "payload": games,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find games",
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )
