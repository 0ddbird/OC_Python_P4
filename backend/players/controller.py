from backend.players.service import PlayerService
from backend.abstract.typing.model_typing import PrimaryKey, SerializedPlayer


class PlayerController:
    def __init__(self) -> None:
        self.service: PlayerService = PlayerService()

    def get_player(self, id: PrimaryKey) -> SerializedPlayer:
        return self.service.get_player(id)

    def create_player(self, player_data) -> PrimaryKey:
        return self.service.create_player(player_data)

    def get_all_players(self) -> tuple[SerializedPlayer]:
        return self.service.get_all_players()

    def update_player(self, player_data: SerializedPlayer) -> None:
        self.service.update_player(player_data)

    def delete_player(self, id: PrimaryKey) -> None:
        self.service.delete_player(id)
