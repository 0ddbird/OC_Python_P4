from flask import (
    Blueprint,
    request,
)

from backend.router.tournaments.handlers import (
    handle_get_tournament,
    handle_get_tournaments,
    handle_post_tournament,
)
from backend.router.utils import (
    handle_preflight_request,
    api_response,
)

tournaments_bp = Blueprint("tournaments", __name__, url_prefix="/tournaments")


@tournaments_bp.route(
    "",
    methods=["GET", "POST", "OPTIONS"],
)
def tournaments():
    if request.method == "OPTIONS":
        return handle_preflight_request()
    if request.method == "GET":
        return handle_get_tournaments()
    if request.method == "POST":
        return handle_post_tournament(request)
    return api_response("Error", 400, "Invalid request")


@tournaments_bp.route(
    "/<tournament_id>", methods=["GET", "PUT", "OPTIONS", "DELETE"]
)
def tournament(
    tournament_id,
):
    if request.method == "GET":
        handle_get_tournament(tournament_id)
