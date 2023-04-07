import os
from typing import List, Tuple

from tinydb import TinyDB

from backend.abstract.exceptions.dao_exceptions import PlayerNotFoundException
from backend.abstract.typing.model_typing import PrimaryKey
from backend.players.PlayerModel import PlayerModel
from backend.players.PlayerSerializer import PlayerSerializer


class PlayerDAO:
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("players")
        self.serializer = PlayerSerializer()

    def create_player(self, player: PlayerModel) -> PrimaryKey:
        player = self.serializer.serialize(player)
        return self.table.insert(player)

    def get_player(self, player_id: int) -> PlayerModel:
        player_record = self.table.get(doc_id=player_id)
        if not player_record:
            raise PlayerNotFoundException(player_id)
        player_record["id"] = player_record.doc_id
        return self.serializer.deserialize(player_record)

    def get_players_by_id(self, ids: List[PrimaryKey]) -> Tuple[PlayerModel]:
        players = tuple(self.get_player(id) for id in ids)
        return players

    def get_all_players(self) -> List[PlayerModel]:
        records = self.table.all()
        players = []
        for record in records:
            record["id"] = record.doc_id
            deserialized_player = self.serializer.deserialize(record)
            players.append(deserialized_player)
        return players

    def update_player(self, player: PlayerModel) -> None:
        serialized_player = self.serializer.serialize(player)
        serialized_player.pop("id")
        self.table.update(serialized_player, doc_ids=[player.id])

    def delete_player(self, player_id) -> None:
        self.table.remove(doc_ids=[player_id])
