from flask import Flask
from flask_cors import CORS
from backend.games.GameRoutes import games_bp
from backend.players.PlayerRoutes import players_bp
from backend.rounds.RoundsRoutes import rounds_bp
from backend.tournaments.TournamentRoutes import tournaments_bp


def register_blueprints(app: Flask):
    app.register_blueprint(players_bp)
    app.register_blueprint(tournaments_bp)
    app.register_blueprint(rounds_bp)
    app.register_blueprint(games_bp)


app = Flask(__name__)
CORS(app)
register_blueprints(app)

if __name__ == "__main__":
    app.run(debug=True)
