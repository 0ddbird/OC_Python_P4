from flask import Blueprint, request, Response

from backend.abstract.typing.model_typing import PrimaryKey
from backend.rounds.router import RoundRouter

rounds_blueprint = Blueprint("rounds", __name__, url_prefix="/rounds")
router = RoundRouter()


@rounds_blueprint.route("", methods=["GET"])
def rounds() -> Response:
    match request.method:
        case "GET":
            return router.get_all_rounds()
        case _:
            return router.handle_bad_request()


@rounds_blueprint.route(
    "/<int:round_id>",
    methods=["GET", "POST", "PATCH"],
)
def round(round_id: PrimaryKey) -> Response:
    match request.method:
        case "GET":
            return router.get_round(round_id)
        case "PATCH":
            return router.update_round(round_id, request.json)
        case "POST":
            return router.update_round_games(round_id, request)
        case _:
            return router.handle_bad_request()
