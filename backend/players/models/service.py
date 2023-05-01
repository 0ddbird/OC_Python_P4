from backend.abstract.typing.model_typing import PrimaryKey, SerializedPlayer
from backend.players.dao import PlayerDAO
from backend.players.serializer import PlayerSerializer


class PlayerService:
    def __init__(self) -> None:
        self.dao: PlayerDAO = PlayerDAO()
        self.serializer: PlayerSerializer = PlayerSerializer()

    def get_player(self, id: PrimaryKey) -> SerializedPlayer:
        player = self.dao.get(id)
        return self.serializer.serialize(player)

    def create_player(self, player_data) -> PrimaryKey:
        player = self.serializer.deserialize(player_data)
        return self.dao.create(player)

    def get_all_players(self) -> tuple[SerializedPlayer]:
        players = self.dao.get_all()
        return tuple(self.serializer.serialize(player) for player in players)

    def update_player(self, player_data: SerializedPlayer) -> None:
        player = self.serializer.deserialize(player_data)
        self.dao.update(player)

    def delete_player(self, id: PrimaryKey) -> None:
        self.dao.delete(id)
