from dataclasses import dataclass


@dataclass
class PlayerModel:
    p_id: str
    first_name: str
    last_name: str
    birthdate: tuple[int, int, int]
    elo: int
