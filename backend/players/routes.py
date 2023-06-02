from flask import Blueprint, request, Response
from backend.players.router import PlayerRouter

players_blueprint = Blueprint("players", __name__, url_prefix="/api/players")
player_router = PlayerRouter()


@players_blueprint.route("", methods=["GET", "POST"])
def players() -> Response:
    match request.method:
        case "GET":
            return player_router.get_players()
        case "POST":
            return player_router.create_player(request)
        case _:
            return player_router.handle_bad_request()


@players_blueprint.route("/<int:player_id>", methods=["GET", "PUT", "DELETE"])
def player(player_id) -> Response:
    match request.method:
        case "GET":
            return player_router.get_player(player_id)
        case "PUT":
            return player_router.update_player(player_id, request)
        case "DELETE":
            return player_router.delete_player(player_id)
        case _:
            return player_router.handle_bad_request()
