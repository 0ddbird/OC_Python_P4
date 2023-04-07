import os
from tinydb import TinyDB

from .dao_exceptions import RoundNotFoundException
from ..models.model_typing import PrimaryKey
from ..models.RoundModel import RoundModel
from ..serializers.RoundSerializer import RoundSerializer


class RoundDAO:
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("rounds")
        self.serializer = RoundSerializer()

    def create_round(self, round: RoundModel) -> PrimaryKey:
        serialized_round = self.serializer.serialize(round)
        try:
            del serialized_round["id"]
        except KeyError:
            pass
        return self.table.insert(serialized_round)

    def get_rounds(self) -> list[RoundModel]:
        rounds = self.table.all()
        return [self.serializer.deserialize(round) for round in rounds]

    def get_round(self, round_id: PrimaryKey) -> RoundModel:
        record = self.table.get(doc_id=round_id)
        if record is None:
            raise RoundNotFoundException(round_id)
        record["id"] = record.doc_id
        return self.serializer.deserialize(record)

    def update_round(self, round_id: PrimaryKey, round: RoundModel) -> None:
        raise NotImplementedError
