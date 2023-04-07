from backend.players.PlayerDAO import PlayerDAO
from backend.players.PlayerSerializer import PlayerSerializer
from backend.abstract.exceptions.dao_exceptions import PlayerNotFoundException
from backend.abstract.typing.model_typing import PrimaryKey, SerializedPlayer


class PlayerController:
    def __init__(self) -> None:
        self.dao: PlayerDAO = PlayerDAO()
        self.serializer: PlayerSerializer = PlayerSerializer()

    def create_player(self, player_data) -> PrimaryKey:
        player = self.serializer.deserialize(player_data)
        return self.dao.create_player(player)

    def get_all_players(self) -> tuple[SerializedPlayer]:
        players = self.dao.get_all_players()
        return tuple(self.serializer.serialize(player) for player in players)

    def get_player(self, id: PrimaryKey) -> SerializedPlayer:
        player = self.dao.get_player(id)
        if player is None:
            raise PlayerNotFoundException
        return self.serializer.serialize(player)

    def update_player(self, player_data: SerializedPlayer) -> None:
        player = self.serializer.deserialize(player_data)
        self.dao.update_player(player)

    def delete_player(self, id: PrimaryKey) -> None:
        self.dao.delete_player(id)
