from backend.dao.PlayerDAO import PlayerDAO
from backend.serializers.PlayerSerializer import PlayerSerializer
from ..exceptions.dao import PlayerNotFoundException

from ..exceptions.serializer_exceptions import SerializationException
from ..models.PlayerModel import PlayerModel


class PlayerController:
    def __init__(self):
        self.model = PlayerModel
        self.dao = PlayerDAO()
        self.serializer = PlayerSerializer()

    def create_player(
        self,
        player_data,
    ):
        player = self.serializer.deserialize(player_data)
        record_id = self.dao.create_player(player)
        return record_id

    def get_all_players(self):
        players = self.dao.get_all_players()
        return [self.serializer.serialize(player) for player in players]

    def get_player(self, player_id):
        try:
            player = self.dao.get_player(player_id)
            serialized_player = self.serializer.serialize(player)
            return serialized_player
        except PlayerNotFoundException as e:
            raise PlayerNotFoundException("Player not found") from e
        except SerializationException as e:
            raise SerializationException("Player not serializable") from e

    def update_player(self, player_data):
        player = self.serializer.deserialize(player_data)
        try:
            return self.dao.update_player(player)
        except Exception as e:
            return {"error": str(e)}

    def delete_player(self, player_id):
        try:
            self.dao.delete_player(player_id)
            return {"status": "OK"}
        except Exception as e:
            return {"error": str(e)}
