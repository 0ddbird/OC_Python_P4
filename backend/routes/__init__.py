from flask import Flask
from backend.routes.GameRoutes import games_bp
from backend.routes.PlayerRoutes import players_bp
from backend.routes.RoundsRoutes import rounds_bp
from backend.routes.TournamentRoutes import tournaments_bp


def register_blueprints(app: Flask):
    app.register_blueprint(players_bp)
    app.register_blueprint(tournaments_bp)
    app.register_blueprint(rounds_bp)
    app.register_blueprint(games_bp)
