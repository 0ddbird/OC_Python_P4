from flask import Blueprint, request

from backend.router.players.handlers import (
    handle_delete_player,
    handle_get_player,
    handle_get_players,
    handle_post_player,
    handle_update_player,
)
from backend.router.utils import handle_preflight_request, api_response

players_bp = Blueprint("players", __name__, url_prefix="/players")


@players_bp.route(
    "",
    methods=["GET", "POST", "OPTIONS"],
)
def players():
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "GET":
        return handle_get_players()

    if request.method == "POST":
        return handle_post_player(request)

    return api_response("Error", 400, "Invalid request")


@players_bp.route(
    "/<player_id>",
    methods=["GET", "PUT", "OPTIONS", "DELETE"],
)
def player(player_id):
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "GET":
        return handle_get_player(player_id)

    if request.method == "PUT":
        return handle_update_player(player_id, request)

    if request.method == "DELETE":
        return handle_delete_player(player_id)
