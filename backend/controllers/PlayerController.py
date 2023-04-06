from typing import Tuple

from ..dao.PlayerDAO import PlayerDAO
from ..serializers.PlayerSerializer import PlayerSerializer
from ..exceptions.dao import PlayerNotFoundException
from ..models.model_typing import PrimaryKey


class PlayerController:
    def __init__(self) -> None:
        self.dao: PlayerDAO = PlayerDAO()
        self.serializer: PlayerSerializer = PlayerSerializer()

    def create_player(self, player_data) -> PrimaryKey:
        player = self.serializer.deserialize(player_data)
        return self.dao.create_player(player)

    def get_all_players(self) -> Tuple[dict, ...]:
        players = self.dao.get_all_players()
        return tuple(self.serializer.serialize(player) for player in players)

    def get_player(self, id: PrimaryKey) -> dict:
        try:
            player = self.dao.get_player(id)
            return self.serializer.serialize(player)
        except PlayerNotFoundException as e:
            raise PlayerNotFoundException("Player not found") from e

    def update_player(self, player_data: dict) -> True:
        player = self.serializer.deserialize(player_data)
        self.dao.update_player(player)
        return True

    def delete_player(self, id: PrimaryKey) -> True:
        self.dao.delete_player(id)
        return True
