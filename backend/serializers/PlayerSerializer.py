from datetime import datetime
from backend.models.PlayerModel import PlayerModel

class PlayerSerializer:

    def __init__(self):
        pass

    @staticmethod
    def deserialize(json_data):
        chess_id = json_data["chess_id"]
        first_name = json_data["first_name"]
        last_name = json_data["last_name"]
        birthdate = datetime.strptime(json_data["birthdate"], "%Y-%m-%d").date()
        elo = int(json_data["elo"])
        print(birthdate)

        if chess_id is None:
            raise ValueError("Chess ID is None")
        if first_name is None:
            raise ValueError("First name is None")
        if last_name is None:
            raise ValueError("Last name is None")
        if birthdate is None:
            raise ValueError("Birthdate is None")
        if elo is None:
            raise ValueError("ELO is None")

        return PlayerModel(chess_id, first_name, last_name, birthdate, elo)

    @staticmethod
    def serialize(player):
        # Serialization from Model to TinyDB json
        if player.id is None:
            return {
                "chess_id": player.chess_id,
                "first_name": player.first_name,
                "last_name": player.last_name,
                "birthdate": player.birthdate.strftime("%Y-%m-%d"),
                "elo": player.elo
            }
        # Serialization from Model to View
        return {
            "id": player.id,
            "chess_id": player.chess_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birthdate": player.birthdate,
            "elo": player.elo
        }

