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
            record_id = self.dao.create_player(player)
            return record_id
        except Exception as e:
            return {"error": str(e)}

    def get_all_players(self):
        players = self.dao.get_all_players()
        return [self.serializer.serialize(player) for player in players]

    def get_player(self, player_id):
        player = self.dao.get_player(player_id)
        serialized_player = self.serializer.serialize(player)
        return serialized_player

    def update_player(self, player_data, player_id):
        try:
            player = self.serializer.deserialize(player_data)
            return self.dao.update_player(player, player_id)
        except Exception as e:
            return {"error": str(e)}

    def delete_player(self, player_id):
        self.model.delete_player(player_id)
