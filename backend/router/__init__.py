from .routes import players_bp, tournaments_bp


def register_routes(app):
    app.register_blueprint(players_bp)
    app.register_blueprint(tournaments_bp)
