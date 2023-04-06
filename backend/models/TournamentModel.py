from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Optional, Tuple

from backend.models.model_typing import ForeignKey, PrimaryKey


class TournamentStatus(Enum):
    TO_START = (0,)
    STARTED = (1,)
    ROUND_OPEN = (2,)
    ENDED = (3,)


@dataclass
class TournamentModel:
    name: str
    location: str
    description: str
    players_ids: Tuple[ForeignKey, ...]
    max_rounds: int
    rounds: Tuple[ForeignKey, ...] = ()
    current_round: int = 0
    status: TournamentStatus = TournamentStatus.TO_START
    start_datetime: date = datetime.now()
    end_datetime: Optional[date] = None
    id: Optional[PrimaryKey] = None

    def set_to_next_round(self):
        if self.current_round == self.max_rounds:
            raise ValueError("All the rounds are finished.")
        self.current_round += 1

    def set_end_date(self):
        if self.end_datetime is not None:
            raise ValueError("End date is already defined")
        self.end_datetime = datetime.now()
