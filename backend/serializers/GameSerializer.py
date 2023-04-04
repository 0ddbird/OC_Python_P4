from backend.models.GameModel import GameModel, PlayerScore


class GameSerializer:
    def __init__(self):
        pass

    @staticmethod
    def deserialize(json_data):
        try:
            p1_id = json_data["player_1"]
            p2_id = json_data["player_2"]
            p1_score = PlayerScore(json_data["p1_score"])
            p2_score = PlayerScore(json_data["p2_score"])
            r_id = json_data["round_id"]
            g_id = json_data.doc_id

            return GameModel(
                p1_id,
                p2_id,
                r_id,
                p1_score,
                p2_score,
                g_id,
            )
        except Exception as e:
            print(f"GameSerializer: {e}")
            return None

    @staticmethod
    def serialize(game):
        game_id = game.g_id
        player_1_list = game.player_1
        player_2_list = game.player_2

        serialized_game = {
            "game_id": game_id,
            "round_id": game.r_id,
            "player_1": player_1_list,
            "player_2": player_2_list,
        }

        return serialized_game

    @staticmethod
    def serialize_to_db(game):
        serialized_game = {
            "player_1": game.p1_id,
            "p1_score": game.p1_score.value,
            "player_2": game.p2_id,
            "p2_score": game.p2_score.value,
            "round_id": game.r_id,
        }

        return serialized_game
