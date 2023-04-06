from dataclasses import dataclass
from datetime import datetime
from typing import Tuple, Optional

from backend.models.model_typing import ForeignKey, PrimaryKey


@dataclass
class RoundModel:
    games_ids: Tuple[ForeignKey, ...]
    tournament_id: ForeignKey
    round_number: int
    start_datetime: datetime = datetime.now()
    end_datetime: Optional[datetime] = None
    id: Optional[PrimaryKey] = None

    def __post_init__(self):
        if self.tournament_id is None:
            raise ValueError("Tournament ID cannot be None")
        if not isinstance(self.round_number, int) or self.round_number <= 0:
            raise ValueError("Round number must be a positive integer")

    def set_end_datetime(self):
        self.end_datetime = datetime.now()
