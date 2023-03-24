from flask import Flask, request, jsonify, render_template, redirect, url_for, \
    make_response
from flask_cors import CORS
from backend.controllers.PlayerController import PlayerController
from backend.controllers.TournamentController import TournamentController
from backend.exceptions.dao import PlayerCreationException

app = Flask(__name__)
CORS(app)


def handle_preflight_request():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response


@app.route('/player/create', methods=['POST', 'OPTIONS'])
def create_player():
    if request.method == 'OPTIONS':
        return handle_preflight_request()

    controller = PlayerController()
    player = {
        "chess_id": request.json.get('chess_id'),
        "first_name": request.json.get('first_name'),
        "last_name": request.json.get('last_name'),
        "birthdate": request.json.get('birthdate'),
        "elo": request.json.get('elo')
    }
    try:
        controller.create_player(player)
        return {"status": "OK"}
    except PlayerCreationException as e:
        return {
            "status": "Error",
            "code": 400,
            "message": f"Error in playerController: {e}"
        }


@app.route('/player/<player_id>', methods=['GET'])
def get_player(player_id):
    player_controller = PlayerController()
    player = player_controller.get_player(player_id)
    return player


@app.route('/players', methods=['GET'])
def get_players():
    controller = PlayerController()
    players = controller.get_all_players()
    return players


@app.route('/player/<player_id>/update', methods=['PUT'])
def update_player(player_id):
    if request.method == 'OPTIONS':
        return handle_preflight_request()

    player_controller = PlayerController()
    player_data = {
        "player_id": player_id,
        "chess_id": request.json.get('chess_id'),
        "first_name": request.json.get('first_name'),
        "last_name": request.json.get('last_name'),
        "birthdate": request.json.get('birthdate'),
        "elo": request.json.get('elo')
    }
    try:
        updated_player = player_controller.update_player(player_data)
        return {
            "status": "OK",
            "player": updated_player
        }
    except Exception as e:
        return {
            "status": "Not OK",
            "code": 400,
            "message": f"Error in PlayerController: {e}"
        }


@app.route('/tournament/create', methods=['POST', 'OPTIONS'])
def create_tournament():
    if request.method == 'OPTIONS':
        return handle_preflight_request()

    if request.method == 'POST':
        tournament_name = request.json.get('tournament_name')
        # controller = TournamentController()
        # controller.create_tournament(tournament_name)
        return {
            "status_code": 200,
            "message": tournament_name
        }


@app.route('/tournament/<tournament_id>', methods=['GET'])
def get_tournament(tournament_id):
    return {
        "name": "Tournament 1",
        "location": "Location 1",
        "start_date": "2020-01-01",
        "end_date": "2020-01-01",
        "max_rounds": 5,
        "curr_round": 1,
        "players": [
            {
                "first_name": "John",
                "last_name": "Doe",
                "birthdate": "1990-01-01",
                "elo": 1000
            },
            {
                "first_name": "Jane",
                "last_name": "Doe",
                "birthdate": "1990-01-01",
                "elo": 2000
            }
        ],
        "description": "Description 1"
    }
