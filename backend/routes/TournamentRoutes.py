from flask import Blueprint, request, Response

from backend.abstract.typing.model_typing import PrimaryKey
from backend.tournaments.TournamentRouter import TournamentRouter

tournaments_bp = Blueprint("tournaments", __name__, url_prefix="/tournaments")
router = TournamentRouter()


@tournaments_bp.route("", methods=["GET", "POST", "OPTIONS"])
def tournaments() -> Response:
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_tournaments()
        case "POST":
            return router.handle_post_tournament(request)
        case _:
            return router.handle_bad_request()


@tournaments_bp.route(
    "/<int:tournament_id>", methods=["GET", "PUT", "OPTIONS", "DELETE", "POST"]
)
def tournament(tournament_id: PrimaryKey) -> Response:
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_tournament(tournament_id)
        case "POST":
            return router.handle_create_next_round(tournament_id)
        case "DELETE":
            return router.handle_delete_tournament(tournament_id)
        case _:
            return router.handle_bad_request()


@tournaments_bp.route("/<int:tournament_id>/rounds", methods=["GET"])
def tournament_rounds(tournament_id: PrimaryKey) -> Response:
    match request.method:
        case "GET":
            return router.handle_get_tournament_rounds(tournament_id)
        case _:
            return router.handle_bad_request()


@tournaments_bp.route(
    "/<int:tournament_id>/<int:round_number>",
    methods=["GET", "PATCH", "OPTIONS"],
)
def tournament_round(tournament_id: PrimaryKey, round_number: int) -> Response:
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_tournament_round(
                tournament_id,
                round_number,
            )
        case "PATCH":
            return router.handle_update_games(
                tournament_id, round_number, request
            )
        case _:
            return router.handle_bad_request()
