from backend.abstract.classes.dao import DAO
from backend.games.serializer import GameSerializer


class GameDAO(DAO):
    def __init__(self):
        super().__init__(GameSerializer(), "games")
