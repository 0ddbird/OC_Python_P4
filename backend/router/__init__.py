from .players.routes import (
    players_bp,
)
from .tournaments.routes import (
    tournaments_bp,
)


def register_routes(
    app,
):
    app.register_blueprint(players_bp)
    app.register_blueprint(tournaments_bp)
