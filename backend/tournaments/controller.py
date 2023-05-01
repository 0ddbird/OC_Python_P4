from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedTournament,
)

from backend.tournaments.service import TournamentService


class TournamentController:
    def __init__(self) -> None:
        self.service: TournamentService = TournamentService()

    def create_tournament(
        self,
        name: str,
        location: str,
        description: str,
        players_ids: tuple[ForeignKey],
        max_rounds: int,
    ) -> PrimaryKey:
        return self.service.create_tournament(
            name=name,
            location=location,
            description=description,
            players_ids=players_ids,
            max_rounds=max_rounds,
        )

    def get_tournament(
        self, id: PrimaryKey, rounds=False, players=False
    ) -> SerializedTournament:
        return self.service.get_tournament(id, rounds, players)

    def get_all_tournaments(self, rounds=False) -> list[SerializedTournament]:
        return self.service.get_all_tournaments(rounds)

    def create_round(self, tournament_id) -> ForeignKey:
        self.service.create_round(tournament_id)

    def get_round_id(self, tournament_id, round_number):
        return self.service.get_round_id(tournament_id, round_number)
