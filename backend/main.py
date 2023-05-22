from flask import Flask, render_template
from flask_cors import CORS
from backend.players.routes import players_blueprint
from backend.games.routes import games_blueprint
from backend.reports.routes import reports_blueprint
from backend.rounds.routes import rounds_blueprint
from backend.tournaments.routes import tournaments_blueprint


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(players_blueprint)
    app.register_blueprint(tournaments_blueprint)
    app.register_blueprint(rounds_blueprint)
    app.register_blueprint(games_blueprint)
    app.register_blueprint(reports_blueprint)


app = Flask(__name__)
register_blueprints(app)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


CORS(app)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
