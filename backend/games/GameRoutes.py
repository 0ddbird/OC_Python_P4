from flask import Blueprint, request

from backend.games.GameRouter import GameRouter

games_bp = Blueprint("games", __name__, url_prefix="/games")
router = GameRouter()


@games_bp.route("", methods=["GET"])
def games():
    match request.method:
        case "GET":
            return router.handle_get_all_games()
        case _:
            return router.handle_bad_request()


@games_bp.route("/<int:game_id>", methods=["GET", "POST", "OPTIONS", "PATCH"])
def game(game_id):
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_game(game_id)
        case "PATCH":
            return router.handle_update_game(game_id, request)
        case _:
            return router.handle_bad_request()


@games_bp.route("/batch", methods=["POST", "OPTIONS"])
def games_by_ids():
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "POST":
            return router.handle_get_games_by_id(request)
        case _:
            return router.handle_bad_request()
