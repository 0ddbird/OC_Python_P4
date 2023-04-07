from datetime import datetime

from backend.abstract.typing.model_typing import SerializedPlayer
from backend.players.PlayerModel import PlayerModel


class PlayerSerializer:
    @staticmethod
    def serialize(player: PlayerModel) -> SerializedPlayer:
        serialized_player = {
            key: getattr(player, key)
            for key in ["chess_id", "first_name", "last_name", "elo"]
        }

        serialized_player["birthdate"] = player.birthdate.strftime("%Y-%m-%d")
        if player.id:
            serialized_player["id"] = player.id
        return serialized_player

    @staticmethod
    def deserialize(json_data: dict) -> PlayerModel:
        chess_id = json_data.get("chess_id")
        first_name = json_data.get("first_name")
        last_name = json_data.get("last_name")
        birthdate_str = json_data.get("birthdate")
        birthdate = datetime.strptime(birthdate_str, "%Y-%m-%d").date()
        elo = int(json_data.get("elo"))
        id = json_data.get("id")
        if id is not None:
            id = int(id)

        return PlayerModel(
            chess_id=chess_id,
            first_name=first_name,
            last_name=last_name,
            birthdate=birthdate,
            elo=elo,
            id=id,
        )
