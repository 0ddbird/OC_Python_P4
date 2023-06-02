import os
import mimetypes

from flask import Flask, render_template, send_from_directory
from flask_cors import CORS
from backend.players.routes import players_blueprint
from backend.games.routes import games_blueprint
from backend.reports.routes import reports_blueprint
from backend.rounds.routes import rounds_blueprint
from backend.tournaments.routes import tournaments_blueprint
from backend.utils.utils import datetime_format


def register_blueprints(app: Flask) -> None:
    app.register_blueprint(players_blueprint)
    app.register_blueprint(tournaments_blueprint)
    app.register_blueprint(rounds_blueprint)
    app.register_blueprint(games_blueprint)
    app.register_blueprint(reports_blueprint)


app = Flask(__name__)
register_blueprints(app)
CORS(app)
app.add_template_filter(datetime_format)


@app.route("/", defaults={"path": ""})
@app.route("/<path:path>")
def serve(path):
    if path != "" and os.path.exists("static/build/" + path):
        mimetype = mimetypes.guess_type(path)[0]
        print(f"Serving {path} with MIME type {mimetype}")
        return send_from_directory("static/build", path)
    else:
        return send_from_directory("static/build", "index.html")


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True, port=5000)
