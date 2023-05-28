from flask import make_response, Request, Response
from backend.abstract.classes.router import Router
from backend.abstract.response_codes import ResCode
from backend.abstract.typing.model_typing import PrimaryKey
from backend.games.controller import GameController


class GameRouter(Router):
    def __init__(self):
        self.controller = GameController()

    def get_game(self, game_id: PrimaryKey) -> Response:
        try:
            game = self.controller.get(game_id)
            return make_response(
                {"message": "Game found", "payload": game}, ResCode.OK.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find game"}, ResCode.BAD_REQUEST.value
            )

    def get_all_games(self):
        try:
            games = self.controller.get_all()
            return make_response(
                {"message": "Games found", "payload": games}, ResCode.OK.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find games"}, ResCode.BAD_REQUEST.value
            )

    def update_game(self, game_id: PrimaryKey, request: Request) -> Response:
        try:
            p1_score = request.json.get("p1_score")
            print(game_id, p1_score)
            self.controller.update(game_id, p1_score)
            return make_response(
                {"message": "Game updated"}, ResCode.NO_CONTENT.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find game"}, ResCode.BAD_REQUEST.value
            )

    def get_games_by_id(self, request: Request) -> Response:
        try:
            games_ids = request.json.get("games_ids")
            games = self.controller.get_multiple(games_ids)
            return make_response(
                {"message": "Games found", "payload": games}, ResCode.OK.value
            )
        except Exception as e:
            print(str(e))
            return make_response(
                {"message": "Can't find games"}, ResCode.BAD_REQUEST.value
            )
