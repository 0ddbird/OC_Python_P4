from flask import Blueprint, request, Response
from backend.reports.router import ReportRouter

reports_blueprint = Blueprint("reports", __name__, url_prefix="/reports")
report_router = ReportRouter()


@reports_blueprint.route("", methods=["GET", "POST"])
def reports() -> Response:
    match request.method:
        case "GET":
            return report_router.get_reports()
        case _:
            return report_router.handle_bad_request()


@reports_blueprint.route("/players", methods=["GET", "POST"])
def player_report() -> Response:
    match request.method:
        case "GET":
            return report_router.get_players()
        case "POST":
            return report_router.post_players()
        case _:
            return report_router.handle_bad_request()


@reports_blueprint.route("/tournaments", methods=["GET", "POST"])
def tournaments_report() -> Response:
    match request.method:
        case "GET":
            return report_router.get_tournaments()
        case "POST":
            return report_router.post_tournaments()
        case _:
            return report_router.handle_bad_request()


@reports_blueprint.route(
    "/tournaments/<int:tournament_id>", methods=["GET", "POST"]
)
def tournament_report(tournament_id) -> Response:
    base = request.args.get("base", "false").lower() == "true"
    players = request.args.get("players", "false").lower() == "true"
    rounds = request.args.get("rounds", "false").lower() == "true"
    match request.method:
        case "GET":
            return report_router.get_tournament(
                tournament_id, base, players, rounds
            )
        case "POST":
            return report_router.post_tournament(
                tournament_id, base, players, rounds
            )
        case _:
            return report_router.handle_bad_request()
