from datetime import datetime
from typing import List


class RoundModel:
    def __init__(self, games_ids: List[int], tournament_id: int, r_num, r_id=None):
        self.r_id = r_id
        self.t_id = tournament_id
        self.r_num = r_num
        self.games_ids = games_ids
        self.start_date = datetime.now()

    def __repr__(self):
        return f"RoundModel({self.r_id}, {self.t_id}, {self.r_num}, {self.r_games_ids}, {self.start_date})"

    def __str__(self):
        return (
            f"RoundModel\n"
            f"{self.r_id=}\n"
            f"{self.t_id=}\n"
            f"{self.r_num=}\n"
            f"{self.games_ids=}\n"
            f"{self.start_date=}"
        )
