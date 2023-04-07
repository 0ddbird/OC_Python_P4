import os
from tinydb import TinyDB

from backend.abstract.exceptions.dao_exceptions import RoundNotFoundException
from backend.abstract.typing.model_typing import PrimaryKey
from backend.rounds.RoundModel import RoundModel
from backend.rounds.RoundSerializer import RoundSerializer


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

    def get_round(self, round_id: PrimaryKey) -> RoundModel:
        record = self.table.get(doc_id=round_id)
        if record is None:
            raise RoundNotFoundException(round_id)
        record["id"] = record.doc_id
        return self.serializer.deserialize(record)

    def get_all_rounds(self) -> list[RoundModel]:
        rounds = self.table.all()
        return [self.serializer.deserialize(round) for round in rounds]

    def get_rounds_by_id(
        self, rounds_ids: tuple[PrimaryKey]
    ) -> tuple[RoundModel]:
        rounds = tuple(self.get_round(id) for id in rounds_ids)
        return rounds

    def update_round(self, round_id: PrimaryKey, round: RoundModel) -> None:
        raise NotImplementedError
