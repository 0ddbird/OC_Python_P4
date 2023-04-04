from flask import Blueprint, make_response, request

from backend.router.PlayerRouter import PlayerRouter
from backend.router.response_codes import ResCode
from backend.router.TournamentRouter import TournamentRouter


def handle_preflight_request():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add(
        "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
    )
    return response


players_bp = Blueprint("players", __name__, url_prefix="/players")
player_router = PlayerRouter()


@players_bp.route("", methods=["GET", "POST", "OPTIONS"])
def players():
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "GET":
        return player_router.handle_get_players()

    if request.method == "POST":
        return player_router.handle_post_player(request)

    return make_response({"message": "Bad request"}, ResCode.BAD_REQUEST)


@players_bp.route("/<player_id>", methods=["GET", "PUT", "OPTIONS", "DELETE"])
def player(player_id):
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "GET":
        return player_router.handle_get_player(player_id)

    if request.method == "PUT":
        return player_router.handle_update_player(player_id, request)

    if request.method == "DELETE":
        return player_router.handle_delete_player(player_id)

    return make_response({"message": "Bad request"}, ResCode.BAD_REQUEST)


tournaments_bp = Blueprint("tournaments", __name__, url_prefix="/tournaments")
tournament_router = TournamentRouter()


@tournaments_bp.route("", methods=["GET", "POST", "OPTIONS"])
def tournaments():
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "GET":
        return tournament_router.handle_get_tournaments()

    if request.method == "POST":
        return tournament_router.handle_post_tournament(request)

    return make_response({"message": "Bad request"}, ResCode.BAD_REQUEST)


@tournaments_bp.route(
    "/<tournament_id>", methods=["GET", "PUT", "OPTIONS", "DELETE", "POST"]
)
def tournament(tournament_id):
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "GET":
        return tournament_router.handle_get_tournament(tournament_id)

    if request.method == "POST":
        return tournament_router.handle_next_round(tournament_id)

    return make_response({"message": "Bad request"}, ResCode.BAD_REQUEST)
