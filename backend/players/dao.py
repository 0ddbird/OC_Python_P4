from backend.abstract.classes.dao import DAO
from backend.players.serializer import PlayerSerializer


class PlayerDAO(DAO):
    def __init__(self):
        super().__init__(PlayerSerializer(), "players")
