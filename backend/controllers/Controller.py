from controllers.GameController import (
    GameController,
)
from controllers.PlayerController import (
    PlayerController,
)
from controllers.RoundController import (
    RoundController,
)
from controllers.TournamentController import (
    TournamentController,
)


class Controller:
    def __init__(
        self,
    ):
        self.player_controller = PlayerController()
        self.tournament_controller = TournamentController()
        self.round_controller = RoundController()
        self.game_controller = GameController()
