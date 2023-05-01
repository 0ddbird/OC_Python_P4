from dataclasses import dataclass
from enum import Enum
from typing import Optional

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey


class GameUpdateException(Exception):
    pass


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
    tournament_id: Optional[ForeignKey] = None
    status: GameStatus = GameStatus.OPEN
    id: Optional[PrimaryKey] = None

    def set_id(self, id: PrimaryKey) -> None:
        self.id = id

    def set_round_id(self, round_id: ForeignKey) -> None:
        self.round_id = round_id

    def is_over(self):
        return self.status == GameStatus.OVER

    def set_results(self, p1_score) -> None:
        if self.is_over():
            raise GameUpdateException
        scores = [0.0, 0.5, 1.0]
        if p1_score not in scores:
            raise ValueError
        self.p1_score = PlayerScore(p1_score)
        self.p2_score = PlayerScore(1.0 - p1_score)
        self.close()

    def close(self):
        self.status = GameStatus.OVER

    def get_player_results(self):
        return {self.p1_id: self.p1_score, self.p2_id: self.p2_score}

    def rank_players(self, ranking, history) -> None:
        players = [
            (self.p1_id, self.p1_score.value, self.p2_id),
            (self.p2_id, self.p2_score.value, self.p1_id),
        ]

        for player_id, score, opponent in players:
            if player_id not in history:
                history[player_id] = []

            history[player_id].append(opponent)
            ranking[player_id] += score
