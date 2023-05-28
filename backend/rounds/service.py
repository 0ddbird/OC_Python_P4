from typing import Iterable

from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedRound,
)
from backend.games.dao import GameDAO
from backend.games.serializer import GameSerializer
from backend.rounds.dao import RoundDAO
from backend.rounds.model import RoundModel
from backend.rounds.serializer import RoundSerializer


class RoundService:
    def __init__(self):
        self.dao: RoundDAO = RoundDAO()
        self.game_dao: GameDAO = GameDAO()
        self.game_serializer: GameSerializer = GameSerializer()
        self.serializer: RoundSerializer = RoundSerializer(
            self.game_serializer
        )

    def get_round(self, id: PrimaryKey, games=False) -> SerializedRound:
        round = self.dao.get(id)
        if games:
            self.set_round_games(round)
        return self.serializer.serialize(round)

    def get_all_rounds(self, games=False) -> list[SerializedRound]:
        rounds = self.dao.get_all_rounds()

        if games:
            for round in rounds:
                self.set_round_games(round)
        return [self.serializer.serialize(round) for round in rounds]

    def get_tournament_rounds(
        self, ids: Iterable[ForeignKey], games=False
    ) -> list[RoundModel]:
        rounds = self.dao.get_multiple(ids)
        if games:
            for round in rounds:
                self.set_round_games(round)
        return rounds

    def set_round_games(self, round: RoundModel) -> None:
        games = self.game_dao.get_multiple(round.games_ids)
        if games:
            round.set_games(games)

    def create_round(
        self,
        games_ids: Iterable[PrimaryKey],
        tournament_id: ForeignKey,
        round_number: int,
    ) -> PrimaryKey:
        round = RoundModel(
            games_ids=games_ids,
            tournament_id=tournament_id,
            round_number=round_number,
        )
        return self.dao.create(round)
