import os
from datetime import date

from tinydb import TinyDB, Query
from backend.models.PlayerModel import PlayerModel
from backend.serializers.PlayerSerializer import PlayerSerializer
from typing import List


class PlayerNotFoundException(Exception):
    pass


class PlayerDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "players.json"))
        self.serializer = PlayerSerializer()

    def create_player(self, player_model: PlayerModel):
        try:
            # Propre à TinyDB
            player = self.serializer.serialize(player_model)
            record_id = self.db.insert(player)
            return record_id
        except Exception as e:
            print(e)
            raise

    def get_all_players(self) -> List[PlayerModel]:
        players = self.db.all()
        player_models = [PlayerModel(**player, id=player.doc_id) for player in
                         players]
        return player_models

    def get_player(self, player_id):
        try:
            result = self.db.get(doc_id=player_id)
            if result:
                player = PlayerModel(
                    chess_id=result['chess_id'],
                    first_name=result['first_name'],
                    last_name=result['last_name'],
                    birthdate=date.fromisoformat(result['birthdate']),
                    elo=result['elo'],
                    id=result.doc_id
                )
                return player
            else:
                raise PlayerNotFoundException(f"Player with id {player_id} "
                                              f"not found")
        except KeyError:
            return None

    def update_player(self, player_id, updated_player):
        user = Query()
        result = self.db.update(updated_player, user.doc_id == player_id)
        print(result)
        return result

    def delete_player(self, player_id):
        user = Query()
        self.db.remove(user.doc_id == player_id)
