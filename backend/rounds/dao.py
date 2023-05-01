from backend.abstract.classes.dao import DAO
from backend.games.serializer import GameSerializer
from backend.rounds.serializer import RoundSerializer


class RoundDAO(DAO):
    def __init__(self):
        super().__init__(RoundSerializer(GameSerializer()), "rounds")
