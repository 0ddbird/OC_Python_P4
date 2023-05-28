from backend.abstract.classes.dao import DAO
from backend.games.serializer import GameSerializer
from backend.rounds.serializer import RoundSerializer


class RoundDAO(DAO):
    def __init__(self):
        super().__init__(RoundSerializer(GameSerializer()), "rounds")

    @staticmethod
    def pop_games(obj: dict):
        try:
            del obj["games"]
        except KeyError:
            pass

    def update(self, model):
        serialized_model = self.serializer.serialize(model)
        self.pop_id(serialized_model)
        self.pop_games(serialized_model)
        with self.open_db() as table:
            table.update(serialized_model, doc_ids=[model.id])
