from flask import Blueprint, request, Response

from backend.abstract.typing.model_typing import PrimaryKey
from backend.games.router import GameRouter

games_blueprint = Blueprint("games", __name__, url_prefix="/api/games")
router = GameRouter()


@games_blueprint.route("", methods=["GET"])
def games() -> Response:
    match request.method:
        case "GET":
            return router.get_all_games()
        case _:
            return router.handle_bad_request()


@games_blueprint.route(
    "/<int:game_id>",
    methods=["GET", "POST", "PATCH"],
)
def game(game_id: PrimaryKey) -> Response:
    match request.method:
        case "GET":
            return router.get_game(game_id)
        case "PATCH":
            return router.update_game(game_id, request)
        case _:
            return router.handle_bad_request()


@games_blueprint.route("/batch", methods=["POST"])
def games_by_ids() -> Response:
    match request.method:
        case "POST":
            return router.get_games_by_id(request)
        case _:
            return router.handle_bad_request()
