from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Iterable, Optional

from backend.abstract.typing.model_typing import (
    ForeignKey,
    Key,
    PrimaryKey,
    Score,
)
from backend.players.model import PlayerModel
from backend.rounds.model import RoundModel
from backend.tournaments.utils import (
    sort_and_pair_players,
    shuffle_and_pair_players,
)


class TournamentStatus(Enum):
    TO_START = (0,)
    STARTED = (1,)
    ROUND_OPEN = (2,)
    ENDED = (3,)


class RoundStartException(Exception):
    pass


@dataclass
class TournamentModel:
    name: str
    location: str
    description: str
    players_ids: tuple[ForeignKey, ...]
    max_rounds: int
    rounds_ids: tuple[ForeignKey, ...] = ()
    current_round: int = 0
    status: TournamentStatus = TournamentStatus.TO_START
    start_datetime: date = datetime.now()
    end_datetime: Optional[date] = None
    id: Optional[PrimaryKey] = None
    rounds: Optional[list[RoundModel]] = None
    leaderboard: Optional[list[tuple[float, ForeignKey]]] = None
    players: Optional[list[PlayerModel]] = None

    def set_rounds(self, rounds: Iterable[RoundModel]) -> None:
        for round in rounds:
            if not isinstance(round, RoundModel):
                raise TypeError("Not instance of Round Model")
        self.rounds = rounds

    def pair_players(self) -> list[tuple[ForeignKey]]:
        if self.status == TournamentStatus.TO_START:
            pairs = shuffle_and_pair_players(self.players_ids)
            return pairs

        if self.status == TournamentStatus.STARTED:
            player_scores, history = self.get_leaderboard_and_history()
            pairs = sort_and_pair_players(player_scores, history)
            return pairs
        raise RoundStartException

    def set_rounds_ids(self, rounds_ids: tuple[ForeignKey]) -> None:
        self.rounds_ids = rounds_ids

    def set_status_open(self) -> None:
        self.status = TournamentStatus.ROUND_OPEN
        self.current_round += 1

    def set_status_started(self) -> None:
        self.status = TournamentStatus.STARTED

    def has_remaining_rounds(self) -> bool:
        return self.current_round < self.max_rounds

    def end(self) -> None:
        if self.end_datetime is not None:
            raise ValueError("End date is already defined")
        self.end_datetime = datetime.now()
        self.status = TournamentStatus.ENDED

    def get_leaderboard_and_history(
            self,
    ) -> tuple[list[tuple[Key, Score]], dict[PrimaryKey, list[ForeignKey]]]:
        player_scores = {player_id: 0.0 for player_id in self.players_ids}
        history = {}
        for round in self.rounds:
            round.rank_players(player_scores, history)
        player_scores = [
            (score, player_id) for player_id, score in player_scores.items()
        ]
        self.leaderboard = player_scores
        return player_scores, history
