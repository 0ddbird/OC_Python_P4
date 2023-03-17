import os
from tinydb import TinyDB, Query
from backend.models.PlayerModel import PlayerModel
from backend.serializers.PlayerSerializer import PlayerSerializer
from typing import List

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
        player_models = [
            PlayerModel(**player, id=player.doc_id) for player in players
                         ]
        return player_models

    def get_player(self, player_id):
        # Renvoyer PlayerModel(result)
        # Vérifier le type d'erreur TinyDB si player n'existe pas
        try:
            result = self.db.search(Query().doc_id == player_id)
            return PlayerModel(result)
        except Error as e:
            print(e)
            return None

    def update_player(self, player_id, updated_player):
        user = Query()
        self.db.update(updated_player, user.doc_id == player_id)

    def delete_player(self, player_id):
        user = Query()
        self.db.remove(user.doc_id == player_id)