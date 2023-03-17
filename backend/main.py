import sys
from flask import Flask, request, jsonify, render_template, redirect, url_for
from backend.controllers.PlayerController import PlayerController
from backend.controllers.TournamentController import TournamentController

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return render_template('views/index.html')

@app.route('/players', methods=['GET'])
def get_players():
    controller = PlayerController()
    players = controller.get_all_players()
    return render_template('views/players_list.html', players=players)

@app.route('/player/create', methods=['GET', 'POST'])
def create_player():
    controller = PlayerController()
    if request.method == 'POST':
        chess_id = request.form['chess_id']
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birthdate = request.form['birthdate']
        elo = request.form['elo']
        try:
            controller.create_player({
                "chess_id": chess_id,
                "first_name": first_name,
                "last_name": last_name,
                "birthdate": birthdate,
                "elo": elo
            })
            return redirect(url_for('get_players'))
        except Exception as e:
            return {
                "status": "Not OK",
                "code": 400,
                "message": f"Error in playerController: {e}"
            }
    return render_template('views/create_player.html')

@app.route('/tournament/create', methods=['GET','POST'])
def create_tournament():

    if request.method == 'GET':
        player_controller = PlayerController()
        players = player_controller.get_all_players()

        return render_template('views/create_tournament.html', players=players)
    if request.method == 'POST':
        players_ids = request.form["players"]
        tournament_controller = TournamentController()
        tournament_controller.create_tournament(players_ids)

@app.route('/player/<player_id>', methods=['GET'])
def get_player(player_id):
    return {
        "first_name": "John",
        "last_name": "Doe",
        "birthdate": "1990-01-01",
        "elo": 1000
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



@app.route('/reports', methods=['GET'])
def get_reports():
    pass
