from flask import Blueprint, request

from backend.rounds.RoundRouter import RoundRouter

rounds_bp = Blueprint("rounds", __name__, url_prefix="/rounds")
router = RoundRouter()


@rounds_bp.route("", methods=["GET"])
def rounds():
    match request.method:
        case "GET":
            return router.handle_get_all_rounds()
        case _:
            return router.handle_bad_request()


@rounds_bp.route("/<int:round_id>", methods=["GET", "POST", "OPTIONS"])
def round(round_id):
    match request.method:
        case "OPTIONS":
            return router.handle_preflight_request()
        case "GET":
            return router.handle_get_round(round_id)
        case "PATCH":
            return router.handle_update_round(round_id, request.json)
        case _:
            return router.handle_bad_request()
