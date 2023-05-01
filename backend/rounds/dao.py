import os
from typing import Iterable

from tinydb import TinyDB

from backend.abstract.classes.dao import DAO
from backend.abstract.exceptions.dao_exceptions import RoundNotFoundException
from backend.abstract.typing.model_typing import PrimaryKey
from backend.games.dao import GameDAO
from backend.rounds.models.model import RoundModel
from backend.rounds.serializer import RoundSerializer


class RoundDAO(DAO):
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("rounds")
        self.game_dao = GameDAO()
        self.serializer = RoundSerializer()

    def create_round(self, round: RoundModel) -> PrimaryKey:
        serialized_round = self.serializer.serialize(round)
        self.pop_id(serialized_round)
        return self.table.insert(serialized_round)

    def get_round(self, id: PrimaryKey) -> RoundModel:
        record = self.table.get(doc_id=id)
        if record is None:
            raise RoundNotFoundException(id)
        record["id"] = record.doc_id
        return self.serializer.deserialize(record)

    def get_all_rounds(self) -> Iterable[RoundModel]:
        rounds = self.table.all()
        return [self.serializer.deserialize(round) for round in rounds]

    def get_multiple_rounds(
        self, ids: Iterable[PrimaryKey]
    ) -> tuple[RoundModel]:
        rounds = tuple(self.get_round(id) for id in ids)
        return rounds

    def update_round(self, id: PrimaryKey, round: RoundModel) -> None:
        serialized_round = self.serializer.serialize(round)
        self.pop_id(serialized_round)
        self.table.update(serialized_round, doc_ids=[id])

    def delete_round(self, id: PrimaryKey) -> None:
        self.table.remove(doc_ids=[id])
