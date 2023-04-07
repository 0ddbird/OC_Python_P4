from datetime import date
from dataclasses import dataclass
from typing import Optional
from backend.abstract.typing.model_typing import ChessID, PrimaryKey


@dataclass
class PlayerModel:
    chess_id: ChessID
    first_name: str
    last_name: str
    birthdate: date
    elo: int
    id: Optional[PrimaryKey] = None

    def __post_init__(self) -> None:
        if not ChessID.match(self.chess_id):
            raise ValueError("Invalid chess ID format")
