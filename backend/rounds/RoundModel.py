from dataclasses import dataclass
from datetime import datetime
from enum import Enum
from typing import Optional

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey


class RoundStatus(Enum):
    OPEN = (0,)
    CLOSED = (1,)


@dataclass
class RoundModel:
    games_ids: tuple[ForeignKey, ...]
    tournament_id: ForeignKey
    round_number: int = 0
    status: RoundStatus = RoundStatus.OPEN
    start_datetime: datetime = datetime.now()
    end_datetime: Optional[datetime] = None
    id: Optional[PrimaryKey] = None

    def __post_init__(self) -> None:
        if self.tournament_id is None:
            raise ValueError("Tournament ID cannot be None")

    def set_end_datetime(self) -> None:
        self.end_datetime = datetime.now()
