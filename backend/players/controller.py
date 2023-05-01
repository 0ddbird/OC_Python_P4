from backend.players.models.service import PlayerService
from backend.abstract.typing.model_typing import PrimaryKey, SerializedPlayer


class PlayerController:
    def __init__(self) -> None:
        self.service: PlayerService = PlayerService()

    def get(self, id: PrimaryKey) -> SerializedPlayer:
        return self.service.get(id)

    def create(self, player_data) -> PrimaryKey:
        return self.service.create(player_data)

    def get_all(self) -> tuple[SerializedPlayer]:
        return self.service.get_all()

    def update(self, player_data: SerializedPlayer) -> None:
        return self.service.update(player_data)

    def delete(self, id: PrimaryKey) -> None:
        self.service.delete(id)
