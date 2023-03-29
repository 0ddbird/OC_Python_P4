from flask import (
    Flask,
    request,
    jsonify,
    render_template,
    redirect,
    url_for,
    make_response,
)
from flask_cors import CORS
from backend.controllers.PlayerController import PlayerController
from backend.controllers.TournamentController import TournamentController
from backend.exceptions.dao import PlayerCreationException
from backend.middleware.validate_tournament_payload import (
    TournamentValidationException,
    validate_tournament_fields,
)

app = Flask(__name__)
CORS(app)


def handle_preflight_request():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add("Access-Control-Allow-Methods", "POST")
    return response


@app.route("/player/create", methods=["POST", "OPTIONS"])
def create_player():
    if request.method == "OPTIONS":
        return handle_preflight_request()

    controller = PlayerController()
    player = {
        "chess_id": request.json.get("chess_id"),
        "first_name": request.json.get("first_name"),
        "last_name": request.json.get("last_name"),
        "birthdate": request.json.get("birthdate"),
        "elo": request.json.get("elo"),
    }
    try:
        player_id = controller.create_player(player)
        return {"status": "OK", "status_code": 200, "id": player_id}
    except PlayerCreationException as e:
        return {
            "status": "Error",
            "code": 400,
            "message": f"Error in playerController: {e}",
        }


@app.route("/player/<player_id>", methods=["GET"])
def get_player(player_id):
    player_controller = PlayerController()
    player = player_controller.get_player(player_id)
    return player


@app.route("/players", methods=["GET"])
def get_players():
    controller = PlayerController()
    players = controller.get_all_players()
    return players


@app.route("/player/<player_id>/update", methods=["PUT"])
def update_player(player_id):
    if request.method == "OPTIONS":
        return handle_preflight_request()

    player_controller = PlayerController()
    player_data = {
        "player_id": player_id,
        "chess_id": request.json.get("chess_id"),
        "first_name": request.json.get("first_name"),
        "last_name": request.json.get("last_name"),
        "birthdate": request.json.get("birthdate"),
        "elo": request.json.get("elo"),
    }

    try:
        updated_player_id = player_controller.update_player(player_data)
        return {
            "status": "OK",
            "status_code": 200,
            "player_id": updated_player_id
        }
    except Exception as e:
        return {
            "status": "Not OK",
            "status_code": 400,
            "message": f"Error in PlayerController: {e}",
        }


@app.route("/player/<player_id>/delete", methods=["DELETE"])
def delete_player(player_id):
    if request.method == "OPTIONS":
        return handle_preflight_request()

    player_controller = PlayerController()
    try:
        player_controller.delete_player(int(player_id))
        return {"status": "OK"}
    except Exception as e:
        return {
            "status": "Not OK",
            "code": 400,
            "message": f"Error in PlayerController: {e}",
        }


@app.route("/tournament/create", methods=["POST", "OPTIONS"])
def create_tournament():
    if request.method == "OPTIONS":
        return handle_preflight_request()

    if request.method == "POST":
        name = request.json.get("name")
        rounds = request.json.get("rounds")
        location = request.json.get("location")
        description = request.json.get("description")
        players_ids = request.json.get("players_ids")

        try:
            validate_tournament_fields(name, rounds, location, description, players_ids)
        except TournamentValidationException as e:
            return {
                "status": "Not OK",
                "code": 400,
                "message": f"Error in TournamentController: {e}",
            }

        try:
            controller = TournamentController()
            tournament_id = controller.create_tournament(
                name, rounds, location, description, players_ids
            )
            return {
                "status": "OK",
                "status_code": 200,
                "tournament_id": tournament_id
            }

        except Exception as e:
            return {
                "status": "Not OK",
                "code": 400,
                "message": f"Error in TournamentController: {e}",
            }


    return {"status_code": 400, "message": "Bad request"}


@app.route("/tournament/<tournament_id>", methods=["GET"])
def get_tournament(tournament_id):
    controller = TournamentController()
    try:
        serialized_tournament = controller.get_tournament(tournament_id)
        return {"status": "OK", "status_code": 200, "tournament": serialized_tournament}
    except Exception as e:
        return {
            "status": "Not OK",
            "code": 400,
            "message": f"Error in TournamentController: {e}",
        }

@app.route("/tournaments", methods=["GET"])
def get_tournaments():
    controller = TournamentController()
    try:
        serialized_tournaments = controller.get_all_tournaments()
        return {"status": "OK", "status_code": 200, "tournaments": serialized_tournaments}
    except Exception as e:
        return {
            "status": "Not OK",
            "code": 400,
            "message": f"Error in TournamentController: {e}",
        }
