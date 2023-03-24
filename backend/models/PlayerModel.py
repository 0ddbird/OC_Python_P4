from datetime import date


class PlayerModel:
    def __init__(self, chess_id: int, first_name: str, last_name: str,
                 birthdate: date, elo: int, player_id=None):
        self.player_id = player_id
        self.chess_id = chess_id
        self.first_name = first_name
        self.last_name = last_name
        self.birthdate = birthdate
        self.elo = elo

    def __repr__(self):
        return str(self.as_dict())

    def as_dict(self):
        return {
            "player_id": self.player_id,
            "chess_id": self.chess_id,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "birthdate": self.birthdate,
            "elo": self.elo
        }
