from backend.abstract.classes.Router import Router
from backend.games.GameController import GameController


class GameRouter(Router):
    def __init__(self):
        self.controller = GameController()
