from flask import Flask, request, jsonify, render_template, redirect, url_for, \
    make_response
from flask_cors import CORS
from backend.controllers.PlayerController import PlayerController
from backend.controllers.TournamentController import TournamentController

app = Flask(__name__)
CORS(app)


def handle_preflight_request():
    response = make_response()
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
    response.headers.add('Access-Control-Allow-Methods', 'POST')
    return response


@app.route('/players', methods=['GET'])
def get_players():
    controller = PlayerController()
    players = controller.get_all_players()
    return players


@app.route('/player/create', methods=['POST', 'OPTIONS'])
def create_player():
    if request.method == 'OPTIONS':
        return handle_preflight_request()

    controller = PlayerController()

    chess_id = request.json.get('chess_id')
    first_name = request.json.get('first_name')
    last_name = request.json.get('last_name')
    birthdate = request.json.get('birthdate')
    elo = request.json.get('elo')
    try:
        controller.create_player({
            "chess_id": chess_id,
            "first_name": first_name,
            "last_name": last_name,
            "birthdate": birthdate,
            "elo": elo
        })
        return {"status": "OK"}
    except Exception as e:
        return {
            "status": "Not OK",
            "code": 400,
            "message": f"Error in playerController: {e}"
        }


@app.route('/tournament/create', methods=['POST', 'OPTIONS'])
def create_tournament():
    if request.method == 'OPTIONS':
        return handle_preflight_request()

    if request.method == 'POST':
        tournament_name = request.json.get('tournament_name')
        controller = TournamentController()
        controller.create_tournament(tournament_name)
        return {
            "status_code": 200,
            "message": tournament_name
        }


@app.route('/player/<player_id>', methods=['GET'])
def get_player(player_id):
    player_controller = PlayerController()
    player = player_controller.get_player(player_id)
    return player


@app.route('/player/<player_id>/update', methods=['POST'])
def update_player(player_id):
    player_controller = PlayerController()
    player = player_controller.get_player(player_id)
    if player:
        try:
            chess_id = request.form['chess_id']
            first_name = request.form['first_name']
            last_name = request.form['last_name']
            birthdate = request.form['birthdate']
            elo = request.form['elo']

            player_id = player.id
            player_data = {
                "chess_id": chess_id,
                "first_name": first_name,
                "last_name": last_name,
                "birthdate": birthdate,
                "elo": elo
            }

            player_controller.update_player(player_data, player_id)
            return {"status": "OK"}
        except Exception as e:
            return {
                "status": "Not OK",
                "code": 400,
                "message": f"Error in playerController: {e}"
            }


@app.route('/tournaments', methods=['GET'])
def get_tournaments():
    pass


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
