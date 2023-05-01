from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Iterable, Optional

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey
from backend.games.models.GameModel import GameModel


class RoundStatus(Enum):
    OPEN = (0,)
    CLOSED = (1,)


@dataclass
class RoundModel:
    games_ids: Iterable[ForeignKey]
    tournament_id: ForeignKey
    round_number: int = 0
    status: RoundStatus = RoundStatus.OPEN
    start_datetime: datetime = datetime.now()
    end_datetime: Optional[datetime] = None
    id: Optional[PrimaryKey] = None
    games: Optional[list[GameModel]] = None

    def __post_init__(self) -> None:
        if self.tournament_id is None:
            raise ValueError("Tournament ID cannot be None")

    def set_games(self, games: Iterable[GameModel]):
        self.games = games

    def end(self):
        self.end_datetime = datetime.now()
        self.status = RoundStatus.CLOSED

    def is_over(self) -> bool:
        if self.games is None:
            raise ValueError("Games are not set for this round")

        return all(game.is_over() for game in self.games)

    def rank_players(self, ranking, history):
        for game in self.games:
            game.rank_players(ranking, history)
