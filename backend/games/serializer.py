from backend.games.models.GameModel import GameModel, GameStatus, PlayerScore
from backend.abstract.typing.model_typing import SerializedGame


class GameSerializer:
    @staticmethod
    def serialize(game: GameModel) -> SerializedGame:
        serialized_game = {
            "p1_id": game.p1_id,
            "p2_id": game.p2_id,
            "p1_score": game.p1_score.value,
            "p2_score": game.p2_score.value,
            "round_id": game.round_id,
            "status": game.status.name,
        }
        if game.id:
            serialized_game["id"] = game.id
        return serialized_game

    @staticmethod
    def deserialize(json_data: dict) -> GameModel:
        id = json_data.get("id")
        p1_id = json_data.get("p1_id")
        p2_id = json_data.get("p2_id")
        p1_score = PlayerScore(json_data.get("p1_score"))
        p2_score = PlayerScore(json_data.get("p2_score"))
        round_id = json_data.get("round_id")
        status = GameStatus[json_data.get("status")]

        return GameModel(
            id=id,
            p1_id=p1_id,
            p2_id=p2_id,
            p1_score=p1_score,
            p2_score=p2_score,
            round_id=round_id,
            status=status,
        )
