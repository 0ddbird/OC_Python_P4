from dataclasses import dataclass
from models.PlayerModel import PlayerModel


@dataclass()
class RoundModel:
    r_num: int
    r_players: list[PlayerModel]
