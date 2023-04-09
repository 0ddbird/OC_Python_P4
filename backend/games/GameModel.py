from dataclasses import dataclass
from enum import Enum
from typing import Optional

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey


class PlayerScore(Enum):
    LOSE = 0.0
    TIE = 0.5
    WIN = 1.0
    NONE = None


@dataclass
class GameModel:
    p1_id: ForeignKey
    p2_id: ForeignKey
    p1_score: PlayerScore = PlayerScore.NONE
    p2_score: PlayerScore = PlayerScore.NONE
    round_id: Optional[ForeignKey] = None
    id: Optional[PrimaryKey] = None

    def __post_init__(self) -> None:
        if self.p1_id == self.p2_id:
            raise ValueError("Player IDs must be different.")

    def set_id(self, id: PrimaryKey) -> None:
        self.id = id

    def set_round_id(self, round_id: ForeignKey) -> None:
        self.round_id = round_id

    def set_p1_score(self, score) -> None:
        self.p1_score = PlayerScore(score)

    def set_p2_score(self, score) -> None:
        self.p2_score = PlayerScore(score)
