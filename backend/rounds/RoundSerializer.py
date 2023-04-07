from datetime import datetime

from backend.abstract.typing.model_typing import SerializedRound
from backend.rounds.RoundModel import RoundModel


class RoundSerializer:
    @staticmethod
    def serialize(round: RoundModel) -> SerializedRound:
        serialized_round = {
            key: getattr(round, key)
            for key in [
                "tournament_id",
                "games_ids",
                "start_datetime",
                "end_datetime",
            ]
        }
        serialized_round["start_datetime"] = round.start_datetime.strftime(
            "%Y-%m-%d_%H:%M"
        )
        if round.id:
            serialized_round["id"] = round.id
        return serialized_round

    @staticmethod
    def deserialize(json_data: dict) -> RoundModel:
        id = json_data.get("id")
        games_ids = json_data.get("games_ids")
        tournament_id = json_data.get("tournament_id")
        start_datetime_str = json_data.get("start_datetime")
        start_datetime = datetime.strptime(
            start_datetime_str, "%Y-%m-%d_%H:%M"
        )
        end_datetime_str = json_data.get("end_datetime")
        end_datetime = (
            datetime.strptime(end_datetime_str, "%Y-%m-%d_%H:%M")
            if end_datetime_str
            else None
        )

        return RoundModel(
            id=id,
            games_ids=games_ids,
            tournament_id=tournament_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
        )
