from enum import Enum

player_id = int


class PlayerScore(Enum):
    LOSE = 0.0
    TIE = 0.5
    WIN = 1.0
    NONE = None


class GameModel:
    def __init__(
        self,
        p1_id,
        p2_id,
        r_id=None,
        p1_score=PlayerScore.NONE,
        p2_score=PlayerScore.NONE,
        g_id=None,
    ):
        self.g_id = g_id
        self.p1_id: player_id = p1_id
        self.p2_id: player_id = p2_id
        self.p1_score: PlayerScore = p1_score
        self.p2_score: PlayerScore = p2_score
        self.r_id = r_id

    def set_round_id(self, r_id):
        self.r_id = r_id

    def __repr__(self):
        return (
            f"GameModel\n"
            f"p1_id: {self.p1_id}\n"
            f"p2_id: {self.p2_id}\n"
            f"p1_score: {self.p1_score}\n"
            f"p2_score: {self.p2_score}\n"
            f"r_id: {self.r_id}\n"
            f"g_id: {self.g_id}\n"
        )
