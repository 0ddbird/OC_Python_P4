from dataclasses import dataclass
from datetime import datetime

from models.Model import Model
from models.PlayerModel import PlayerModel


@dataclass
class TournamentModel:
    t_id: str
    name: str
    location: str
    start_date: datetime.date
    end_date: datetime.date
    max_rounds: int
    curr_round: int
    players: list[PlayerModel]
    description: str
