from ..models.PlayerModel import PlayerModel
from backend.serializers.PlayerSerializer import PlayerSerializer
from backend.dao.PlayerDAO import PlayerDAO

class PlayerController:
    def __init__(self):
        self.model = PlayerModel
        self.dao = PlayerDAO()
        self.serializer = PlayerSerializer()

    def create_player(self, player_data):
        try:
            player = self.serializer.deserialize(player_data)
            print(f"PlayerController: create_player called, player={player}")
            record_id = self.dao.create_player(player)
            return {
                "status": "OK",
                "code": 200,
                "p_id": record_id
            }
        except Exception as e:
            return {"error": str(e)}

    def get_all_players(self):
        players = self.dao.get_all_players()
        return [self.serializer.serialize(player) for player in players]

    def get_player(self, player_id):
        return self.model.get_player(player_id)

    def update_player(self, player_id, updated_player):
        self.model.update_player(player_id, updated_player)

    def delete_player(self, player_id):
        self.model.delete_player(player_id)
