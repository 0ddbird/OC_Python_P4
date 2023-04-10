from dataclasses import dataclass
from enum import Enum
from typing import Optional

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey


class GameStatus(Enum):
    OPEN = 0
    OVER = 1


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
    status: GameStatus = GameStatus.OPEN
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

    def end(self):
        self.status = GameStatus.OVER

    def set_players_score(self, p1_score, p2_score) -> None:
        p1_score = PlayerScore(p1_score)
        p2_score = PlayerScore(p2_score)

        score_sum = p1_score.value + p2_score.value
        if score_sum not in [0.0, 1.0, 2.0]:
            raise ValueError(
                "Scores are not consistent or not within the acceptable range."
            )

        if (
            score_sum == 2.0
            and p1_score != PlayerScore.TIE
            and p2_score != PlayerScore.TIE
        ):
            raise ValueError(
                "Scores are not consistent: both players have the same score but it's not a tie."
            )

        self.set_p1_score(p1_score.value)
        self.set_p2_score(p2_score.value)
        self.end()

    def is_over(self):
        return self.status == GameStatus.OVER
