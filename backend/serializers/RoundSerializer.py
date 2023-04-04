from backend.models.RoundModel import RoundModel


class RoundSerializer:
    def __init__(self):
        pass

    @staticmethod
    def deserialize(json_data):
        return RoundModel(
            json_data["player_1"],
            json_data["player_2"],
        )

    @staticmethod
    def serialize(round):
        round.games_ids = round.games_ids
        serialized_round = {
            "round_id": round.r_id,
            "tournament_id": round.t_id,
            "round_number": round.r_num,
            "start_date": round.start_date.strftime("%Y-%m-%d_%H:%M"),
            "games_ids": round.games_ids,
        }

        return serialized_round

    @staticmethod
    def serialize_to_db(round):
        try:
            serialized_round = {
                "tournament_id": round.t_id,
                "round_number": round.r_num,
                "start_date": round.start_date.strftime("%Y-%m-%d_%H:%M"),
                "games_ids": round.games_ids,
            }
        except Exception as e:
            print(e)
        return serialized_round
