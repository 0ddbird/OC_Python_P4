from datetime import datetime
from backend.models.PlayerModel import PlayerModel


class PlayerSerializer:
    def __init__(self):
        pass

    @staticmethod
    def deserialize(json_data):
        player_id = int(json_data.get("player_id")) or None
        chess_id = json_data.get("chess_id")
        first_name = json_data.get("first_name")
        last_name = json_data.get("last_name")
        birthdate_str = json_data.get("birthdate")
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        elo = int(json_data.get("elo"))

        return PlayerModel(chess_id, first_name, last_name, birthdate, elo, player_id)

    @staticmethod
    def serialize(player):
        serialized_player = {
            "player_id": player.player_id,
            "chess_id": player.chess_id,
            "first_name": player.first_name,
            "last_name": player.last_name,
            "birthdate": player.birthdate.strftime("%Y-%m-%d"),
            "elo": player.elo,
        }
        # print(f"Serialized player: {serialized_player}")
        return serialized_player
