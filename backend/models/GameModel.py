from dataclasses import (
    asdict,
)
from enum import (
    Enum,
)


class PlayerScore(Enum):
    LOSE = (0.0,)
    TIE = (0.5,)
    WIN = 1.0


class GameModel:
    def __init__(
        self,
    ):
        self.g_id = None
        self.p_1 = None
        self.p_2 = None
        self.p_1_score = None
        self.p_2_score = None

    def to_dict(
        self,
    ):
        return asdict(self)

    def __str__(
        self,
    ):
        return f"{self.p_1} {self.p_1_score} - {self.p_2_score} {self.p_2}"

    def __repr__(
        self,
    ):
        return f"{self.p_1} {self.p_1_score} - {self.p_2_score} {self.p_2}"
