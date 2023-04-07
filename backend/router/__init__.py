from .routes import players_bp, tournaments_bp, rounds_bp


def register_routes(app):
    app.register_blueprint(players_bp)
    app.register_blueprint(tournaments_bp)
    app.register_blueprint(rounds_bp)
