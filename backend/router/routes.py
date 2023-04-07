from flask import Blueprint, make_response, request, Response

from backend.models.model_typing import PrimaryKey
from backend.router.PlayerRouter import PlayerRouter
from backend.router.response_codes import ResCode
from backend.router.RoundRouter import RoundRouter
from backend.router.TournamentRouter import TournamentRouter


def handle_preflight_request() -> Response:
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
def players() -> Response:
    match request.method:
        case "OPTIONS":
            return handle_preflight_request()
        case "GET":
            return player_router.handle_get_players()
        case "POST":
            return player_router.handle_post_player(request)
        case _:
            return make_response(
                {"message": "Bad request"}, ResCode.BAD_REQUEST.value
            )


@players_bp.route(
    "/<int:player_id>", methods=["GET", "PUT", "OPTIONS", "DELETE"]
)
def player(player_id) -> Response:
    match request.method:
        case "OPTIONS":
            return handle_preflight_request()
        case "GET":
            return player_router.handle_get_player(player_id)
        case "PUT":
            return player_router.handle_update_player(player_id, request)
        case "DELETE":
            return player_router.handle_delete_player(player_id)
        case _:
            return make_response(
                {"message": "Bad request"}, ResCode.BAD_REQUEST.value
            )


tournaments_bp = Blueprint("tournaments", __name__, url_prefix="/tournaments")
tournament_router = TournamentRouter()


@tournaments_bp.route("", methods=["GET", "POST", "OPTIONS"])
def tournaments() -> Response:
    match request.method:
        case "OPTIONS":
            return handle_preflight_request()
        case "GET":
            return tournament_router.handle_get_tournaments()
        case "POST":
            return tournament_router.handle_post_tournament(request)
        case _:
            return make_response(
                {"message": "Bad request"}, ResCode.BAD_REQUEST.value
            )


@tournaments_bp.route(
    "/<int:tournament_id>", methods=["GET", "PUT", "OPTIONS", "DELETE", "POST"]
)
def tournament(tournament_id: PrimaryKey) -> Response:
    match request.method:
        case "OPTIONS":
            return handle_preflight_request()
        case "GET":
            return tournament_router.handle_get_tournament(tournament_id)
        case "POST":
            return tournament_router.handle_create_next_round(tournament_id)
        case "DELETE":
            return tournament_router.handle_delete_tournament(tournament_id)
        case _:
            return make_response(
                {"message": "Bad request"}, ResCode.BAD_REQUEST.value
            )


@tournaments_bp.route(
    "/<int:tournament_id>/rounds", methods=["GET", "POST", "OPTIONS"]
)
def rounds(tournament_id: PrimaryKey) -> Response:
    match request.method:
        case "OPTIONS":
            return handle_preflight_request()
        case "GET":
            return round.router.handle_get_rounds(tournament_id)
        case _:
            return make_response(
                {"message": "Bad request"}, ResCode.BAD_REQUEST.value
            )


rounds_bp = Blueprint("rounds", __name__, url_prefix="/rounds")
round_router = RoundRouter()


@rounds_bp.route("/<int:round_id>", methods=["GET", "PATCH", "OPTIONS"])
def round(round_id: PrimaryKey) -> Response:
    match request.method:
        case "OPTIONS":
            return handle_preflight_request()
        case "GET":
            return round_router.handle_get_round(round_id)
        case "PATCH":
            return round_router.handle_update_round(round_id, request)
        case _:
            return make_response(
                {"message": "Bad request"}, ResCode.BAD_REQUEST.value
            )
