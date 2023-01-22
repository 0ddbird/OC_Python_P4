from enum import Enum
from dataclasses import dataclass
from models.PlayerModel import PlayerModel


class PlayerScore(Enum):
    LOSE = (0.0,)
    TIE = (0.5,)
    WIN = 1.0


@dataclass
class GameModel:
    p_1: PlayerModel
    p_2: PlayerModel
    p_1_score: PlayerScore
    p_2_score: PlayerScore
