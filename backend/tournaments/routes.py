from flask import Blueprint, request, Response

from backend.abstract.typing.model_typing import PrimaryKey
from backend.tournaments.router import TournamentRouter

tournaments_blueprint = Blueprint(
    "tournaments",
    __name__,
    url_prefix="/tournaments",
)
router = TournamentRouter()


@tournaments_blueprint.route(
    "",
    methods=["GET", "POST"],
)
def tournaments() -> Response:
    rounds = request.args.get("rounds", "false").lower() == "true"
    match request.method:
        case "GET":
            return router.get_tournaments(rounds=rounds)
        case "POST":
            return router.create_tournament(request)
        case _:
            return router.handle_bad_request()


@tournaments_blueprint.route(
    "/<int:tournament_id>",
    methods=["GET", "PUT", "DELETE", "POST"],
)
def tournament(tournament_id: PrimaryKey) -> Response:
    players = request.args.get("players", "false").lower() == "true"
    rounds = request.args.get("rounds", "false").lower() == "true"
    match request.method:
        case "GET":
            return router.get_tournament(tournament_id, rounds=rounds, players=players)
        case "POST":
            return router.create_round(tournament_id)
        case "DELETE":
            return router.delete_tournament(tournament_id)
        case _:
            return router.handle_bad_request()


@tournaments_blueprint.route(
    "/<int:tournament_id>/rounds",
    methods=["GET"],
)
def tournament_rounds(tournament_id: PrimaryKey) -> Response:
    match request.method:
        case "GET":
            return router.get_tournament_rounds(tournament_id)
        case _:
            return router.handle_bad_request()


@tournaments_blueprint.route(
    "/<int:tournament_id>/<int:round_number>",
    methods=["GET", "PATCH"],
)
def tournament_round(tournament_id: PrimaryKey, round_number: int) -> Response:
    match request.method:
        case "GET":
            return router.get_tournament_round(
                tournament_id,
                round_number,
            )
        case "PATCH":
            return router.update_games(tournament_id, round_number, request)
        case _:
            return router.handle_bad_request()
