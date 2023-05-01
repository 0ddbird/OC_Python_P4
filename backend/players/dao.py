import os
from typing import List, Tuple

from tinydb import TinyDB

from backend.abstract.classes.dao import DAO
from backend.abstract.exceptions.dao_exceptions import PlayerNotFoundException
from backend.abstract.typing.model_typing import PrimaryKey
from backend.players.models.model import PlayerModel
from backend.players.serializer import PlayerSerializer


class PlayerDAO(DAO):
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("players")
        self.serializer = PlayerSerializer()

    def create(self, player: PlayerModel) -> PrimaryKey:
        player = self.serializer.serialize(player)
        return self.table.insert(player)

    def get(self, id: PrimaryKey) -> PlayerModel:
        player_record = self.table.get(doc_id=id)
        if not player_record:
            raise PlayerNotFoundException(f"Player {id} not found")
        player_record["id"] = player_record.doc_id
        return self.serializer.deserialize(player_record)

    def get_multiple(self, ids: List[PrimaryKey]) -> Tuple[PlayerModel]:
        players = tuple(self.get(id) for id in ids)
        return players

    def get_all(self) -> List[PlayerModel]:
        records = self.table.all()
        players = []
        for record in records:
            record["id"] = record.doc_id
            deserialized_player = self.serializer.deserialize(record)
            players.append(deserialized_player)
        return players

    def update(self, player: PlayerModel) -> None:
        serialized_player = self.serializer.serialize(player)
        self.pop_id(serialized_player)
        self.table.update(serialized_player, doc_ids=[player.id])

    def delete(self, id) -> None:
        self.table.remove(doc_ids=[id])
