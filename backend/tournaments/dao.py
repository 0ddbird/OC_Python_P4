from backend.abstract.classes.dao import DAO
from backend.games.serializer import GameSerializer
from backend.players.serializer import PlayerSerializer
from backend.rounds.serializer import RoundSerializer
from backend.tournaments.serializer import TournamentSerializer


class TournamentDAO(DAO):
    def __init__(self):
        super().__init__(
            TournamentSerializer(
                RoundSerializer(GameSerializer()),
                PlayerSerializer(),
            ),
            "tournaments",
        )

    @staticmethod
    def pop_rounds(obj: dict):
        try:
            del obj["rounds"]
        except KeyError:
            pass

    def update(self, model):
        serialized_model = self.serializer.serialize(model, to_db=True)
        self.pop_id(serialized_model)
        self.pop_rounds(serialized_model)

        with self.open_db() as table:
            table.update(serialized_model, doc_ids=[model.id])
