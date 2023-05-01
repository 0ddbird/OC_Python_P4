from flask import Flask
from flask_cors import CORS
from .players.routing.routes import players_blueprint
from .games.routing.routes import games_blueprint
from .rounds.routing.routes import rounds_blueprint
from .tournaments.routing.routes import tournaments_blueprint


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(players_blueprint)
    app.register_blueprint(tournaments_blueprint)
    app.register_blueprint(rounds_blueprint)
    app.register_blueprint(games_blueprint)


app = Flask(__name__)
register_blueprints(app)
CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
