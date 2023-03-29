from enum import Enum
from dataclasses import dataclass, asdict
from models.PlayerModel import PlayerModel
from dao.GameDAO import GameDAO


class PlayerScore(Enum):
    LOSE = (0.0,)
    TIE = (0.5,)
    WIN = 1.0


class GameModel:
    def __init__(self):
        self.g_id = None
        self.p_1 = None
        self.p_2 = None
        self.p_1_score = None
        self.p_2_score = None
        self.dao = GameDAO()

    def to_dict(self):
        return asdict(self)

    def __str__(self):
        return f"{self.p_1} {self.p_1_score} - {self.p_2_score} {self.p_2}"

    def __repr__(self):
        return f"{self.p_1} {self.p_1_score} - {self.p_2_score} {self.p_2}"

    def create_game(self):
        self.dao.create_game(self)

    def get_game(self, game_id):
        return self.dao.get_game(game_id)

    def update_game(self, game_id, updated_game):
        self.dao.update_game(game_id, updated_game)

    def delete_game(self, game_id):
        self.dao.delete_game(game_id)
