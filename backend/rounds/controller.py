from backend.rounds.models.service import RoundService
from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedRound,
)


class RoundController:
    def __init__(self) -> None:
        self.service: RoundService = RoundService()

    def get_round(self, id: PrimaryKey, rounds=False) -> SerializedRound:
        return self.service.get_round(id, rounds)

    def get_all_rounds(self, games=False) -> list[SerializedRound]:
        return self.service.get_all_rounds(games)

    def create_round(
        self,
        games_ids: list[ForeignKey],
        tournament_id: ForeignKey,
        round_number: int,
    ) -> PrimaryKey:
        return self.service.create_round(
            games_ids, tournament_id, round_number
        )
