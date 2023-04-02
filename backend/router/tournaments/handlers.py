from backend.controllers.TournamentController import TournamentController
from backend.middleware.validate_tournament_payload import (
    TournamentValidationException,
    validate_tournament_fields,
)
from backend.router.utils import api_response

controller = TournamentController()


def handle_get_tournaments():
    try:
        serialized_tournaments = controller.get_all_tournaments()
        return api_response("OK", 200, serialized_tournaments)

    except Exception as e:
        return api_response("Error", 400, f"Error in TournamentController: {e}")


def handle_post_tournament(http_request):
    name = http_request.json.get("name")
    rounds = http_request.json.get("rounds")
    location = http_request.json.get("location")
    description = http_request.json.get("description")
    ids = http_request.json.get("players_ids")

    try:
        validate_tournament_fields(name, rounds, location, description, ids)
    except TournamentValidationException as e:
        return api_response("Error", 400, f"Error in TournamentController: {e}")

    try:
        tournament_id = controller.create_tournament(
            name, rounds, location, description, ids
        )
        return api_response("OK", 201, {"id": tournament_id})

    except Exception as e:
        return api_response("Error", 400, f"Error in TournamentController: {e}")


def handle_get_tournament(tournament_id):
    try:
        serialized_tournament = controller.get_tournament(tournament_id)
        return api_response("OK", 200, serialized_tournament)

    except Exception as e:
        return api_response("Error", 400, f"Error in TournamentController: " f"{e}")
