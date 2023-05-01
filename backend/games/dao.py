import os
from typing import Iterable

from tinydb import TinyDB

from backend.abstract.classes.dao import DAO
from backend.games.models.GameModel import GameModel
from backend.abstract.typing.model_typing import PrimaryKey
from backend.games.serializer import GameSerializer


class GameDAO(DAO):
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("games")
        self.serializer = GameSerializer()

    def create(self, game: GameModel) -> PrimaryKey:
        serialized_game = self.serializer.serialize(game)
        self.pop_id(serialized_game)
        return self.table.insert(serialized_game)

    def get(self, id: PrimaryKey) -> GameModel:
        game_record = self.table.get(doc_id=id)
        game_record["id"] = id
        return self.serializer.deserialize(game_record)

    def get_all(self) -> list[GameModel]:
        records = self.table.all()
        for record in records:
            record["id"] = record.doc_id
        return [self.serializer.deserialize(record) for record in records]

    def get_multiple(self, ids: Iterable[PrimaryKey]):
        return tuple(self.get(id) for id in ids)

    def update(self, updated_game: GameModel):
        serialized_game = self.serializer.serialize(updated_game)
        self.pop_id(serialized_game)
        return self.table.update(serialized_game, doc_ids=[updated_game.id])

    def delete(self, id: PrimaryKey) -> None:
        self.table.remove(doc_ids=[id])
