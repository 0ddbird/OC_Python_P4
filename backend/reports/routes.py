from flask import Blueprint, request, Response
from backend.reports.router import ReportRouter

reports_blueprint = Blueprint("reports", __name__, url_prefix="/reports")
report_router = ReportRouter()


@reports_blueprint.route("/players", methods=["GET"])
def player_report() -> Response:
    match request.method:
        case "GET":
            return report_router.get_players()
        case _:
            return report_router.handle_bad_request()


@reports_blueprint.route("/tournaments", methods=["GET", "POST"])
def tournaments_report() -> Response:
    match request.method:
        case "GET":
            return report_router.get_tournaments()
        case _:
            return report_router.handle_bad_request()


@reports_blueprint.route("/tournaments/<int:tournament_id>", methods=["GET"])
def tournament_report(tournament_id: int):
    if request.method == "GET":
        rounds = request.args.get("rounds", "false").lower() == "true"
        players = request.args.get("players", "false").lower() == "true"
        return report_router.get_tournament(
            tournament_id=tournament_id, players=players, rounds=rounds
        )
    else:
        return report_router.handle_bad_request()
