from backend.models.GameModel import GameModel, PlayerScore


class GameSerializer:
    @staticmethod
    def serialize(game: GameModel) -> dict:
        serialized_game = {
            "p1_id": game.p1_id,
            "p2_id": game.p2_id,
            "p1_score": game.p1_score.name,
            "p2_score": game.p2_score.name,
            "round_id": game.round_id,
        }
        if game.id:
            serialized_game["id"] = game.id
        return serialized_game

    @staticmethod
    def deserialize(json_data: dict) -> GameModel:
        id = json_data.get("id")
        p1_id = json_data.get("p1_id")
        p2_id = json_data.get("p2_id")
        p1_score = PlayerScore[json_data.get("p1_score")]
        p2_score = PlayerScore[json_data.get("p2_score")]
        round_id = json_data.get("round_id")

        return GameModel(
            id=id,
            p1_id=p1_id,
            p2_id=p2_id,
            p1_score=p1_score,
            p2_score=p2_score,
            round_id=round_id,
        )
