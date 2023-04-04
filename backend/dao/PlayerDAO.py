import os
from typing import List

from tinydb import TinyDB

from ..exceptions.dao import PlayerNotFoundException
from ..models.PlayerModel import PlayerModel
from ..serializers.PlayerSerializer import PlayerSerializer


class PlayerDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "players.json"))
        self.serializer = PlayerSerializer()

    def create_player(self, player: PlayerModel):
        player = self.serializer.serialize_to_db(player)
        record_id = self.db.insert(player)
        return record_id

    def get_player(self, player_id: int) -> PlayerModel:
        player_record = self.db.get(doc_id=player_id)
        if not player_record:
            raise PlayerNotFoundException(f"Player with id {player_id} not found")
        player_record["player_id"] = player_id
        return self.serializer.deserialize(player_record)

    def get_selected_players(self, player_ids: List[int]) -> List[PlayerModel]:
        players = []
        for player_id in player_ids:
            player = self.get_player(player_id)
            players.append(player)
        return players

    def get_all_players(self) -> List[PlayerModel]:
        players = self.db.all()
        player_models = []
        for player in players:
            player["player_id"] = player.doc_id
            deserialized_player = self.serializer.deserialize(player)
            player_models.append(deserialized_player)
        return player_models

    def update_player(self, player: PlayerModel):
        serialized_player = self.serializer.serialize(player)
        serialized_player.pop("player_id")
        self.db.update(serialized_player, doc_ids=[player.player_id])
        return player.player_id

    def delete_player(self, player_id):
        self.db.remove(doc_ids=[player_id])
        return "Player deleted", 200
