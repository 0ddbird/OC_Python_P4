from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Iterable, Optional

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey
from backend.rounds.models.model import RoundModel
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

    def set_rounds(self, rounds: Iterable[RoundModel]) -> None:
        for round in rounds:
            if not isinstance(round, RoundModel):
                raise TypeError("Not instance of Round Model")
        self.rounds = rounds

    def pair_players(self) -> list[tuple[ForeignKey]]:
        if self.status == TournamentStatus.TO_START:
            return shuffle_and_pair_players(self.players_ids)
        elif self.status == TournamentStatus.STARTED:
            return sort_and_pair_players(self.player_ids)
        raise RoundStartException

    def set_rounds_ids(self, rounds_ids: tuple[ForeignKey]) -> None:
        self.rounds_ids = rounds_ids

    def set_round_open(self) -> None:
        self.status = TournamentStatus.ROUND_OPEN
        self.current_round += 1

    # def start(self) -> None:
    #     self.status = TournamentStatus.STARTED
    #

    #
    # def set_status_started(self) -> None:
    #     self.status = TournamentStatus.STARTED
    #
    # def set_to_next_round(self) -> None:
    #     if self.current_round == self.max_rounds:
    #         raise ValueError("All the rounds are finished.")
    #     self.current_round += 1
    #
    # def end(self) -> None:
    #     if self.end_datetime is not None:
    #         raise ValueError("End date is already defined")
    #     self.end_datetime = datetime.now()
    #     self.status = TournamentStatus.ENDED
    #
