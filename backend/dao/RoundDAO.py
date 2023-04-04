import os
from tinydb import TinyDB, Query
from ..models.RoundModel import RoundModel
from ..serializers.RoundSerializer import RoundSerializer


class RoundDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "rounds.json"))
        self.serializer = RoundSerializer()

    def create_round(self, round: RoundModel):
        serialized_round = self.serializer.serialize_to_db(round)
        return self.db.insert(serialized_round)

    def get_rounds(self):
        return self.db.all()

    def get_round(self, round_id):
        return self.db.search(Query().r_id.matches(round_id))

    def update_round(self, round_id, updated_round):
        round_ = Query()
        self.db.update(updated_round, round_.r_id.matches(round_id))

    def delete_round(self, round_id):
        round_ = Query()
        self.db.remove(round_.r_id.matches(round_id))
