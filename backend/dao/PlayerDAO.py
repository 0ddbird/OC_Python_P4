import os
from typing import List

from tinydb import TinyDB, Query
from tinydb.table import Document

from backend.exceptions.dao import PlayerNotFoundException
from backend.models.PlayerModel import PlayerModel
from backend.serializers.PlayerSerializer import PlayerSerializer


class PlayerDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "players.json"))
        self.serializer = PlayerSerializer()

    def create_player(self, player: PlayerModel):
        try:
            player = self.serializer.serialize(player)
            record_id = self.db.insert(player)
            return record_id
        except Exception as e:
            print(e)

    def get_player(self, player_id: int) -> PlayerModel:
        try:
            player_record = self.db.get(doc_id=player_id)
            if not player_record:
                raise PlayerNotFoundException(f"Player with id {player_id} not found")
            print(player_record)
            player_record["player_id"] = player_id
            player = self.serializer.deserialize(player_record)
            return player
        except Exception as e:
            print(e)

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
        try:
            self.db.update(serialized_player, doc_ids=[player.player_id])
            return "Player updated", 200
        except Exception as e:
            print(f"Error updating player: {e}")
            return "Player not updated", 500

    def delete_player(self, player_id):
        try:
            self.db.remove(doc_ids=[player_id])
            return "Player deleted", 200
        except Exception as e:
            print(f"Error deleting player: {e}")
            return "Player not deleted", 500
