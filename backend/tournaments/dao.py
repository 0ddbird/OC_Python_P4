from backend.abstract.classes.dao import DAO
from backend.games.serializer import GameSerializer
from backend.players.serializer import PlayerSerializer
from backend.rounds.serializer import RoundSerializer
from backend.tournaments.serializer import TournamentSerializer


class TournamentDAO(DAO):
    def __init__(self):
        super().__init__(
            TournamentSerializer(
                RoundSerializer(GameSerializer()), PlayerSerializer()
            ),
            "tournaments",
        )
