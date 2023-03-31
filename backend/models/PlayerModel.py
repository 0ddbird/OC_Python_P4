from datetime import (
    date,
)


class PlayerModel:
    def __init__(
        self,
        chess_id: str,
        first_name: str,
        last_name: str,
        birthdate: date,
        elo: int,
        player_id=None,
    ):
        self.player_id = player_id
        self.chess_id = chess_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.elo = elo
