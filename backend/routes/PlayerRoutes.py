from flask import Blueprint, request, Response

from backend.players.PlayerRouter import PlayerRouter

players_bp = Blueprint("players", __name__, url_prefix="/players")
router = PlayerRouter()


@players_bp.route("", methods=["GET", "POST", "OPTIONS"])
def players() -> Response:
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_players()
        case "POST":
            return router.handle_post_player(request)
        case _:
            return router.handle_bad_request()


@players_bp.route(
    "/<int:player_id>", methods=["GET", "PUT", "OPTIONS", "DELETE"]
)
def player(player_id) -> Response:
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_player(player_id)
        case "PUT":
            return router.handle_update_player(player_id, request)
        case "DELETE":
            return router.handle_delete_player(player_id)
        case _:
            return router.handle_bad_request()
