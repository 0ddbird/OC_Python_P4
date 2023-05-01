from datetime import datetime
from typing import Optional

from backend.abstract.typing.model_typing import SerializedRound
from backend.games.serializer import GameSerializer
from backend.rounds.models.model import RoundModel, RoundStatus


class RoundSerializer:
    def __init__(self, game_serializer=None):
        self.game_serializer: Optional[GameSerializer] = game_serializer

    def serialize(self, round: RoundModel, to_db=False) -> SerializedRound:
        serialized_round = {
            "games_ids": round.games_ids,
            "tournament_id": round.tournament_id,
            "round_number": round.round_number,
            "start_datetime": round.start_datetime.strftime("%Y-%m-%d_%H:%M"),
            "status": round.status.name,
        }

        if round.end_datetime:
            serialized_round["end_datetime"] = round.end_datetime.strftime(
                "%Y-%m-%d_%H:%M"
            )

        if round.id:
            serialized_round["id"] = round.id

        if round.games and not to_db:
            serialized_round["games"] = [
                self.game_serializer.serialize(game) for game in round.games
            ]
        return serialized_round

    def deserialize(self, json_data: dict) -> RoundModel:
        id = json_data.get("id")
        games_ids = json_data.get("games_ids")
        tournament_id = json_data.get("tournament_id")
        start_datetime_str = json_data.get("start_datetime")
        start_datetime = datetime.strptime(
            start_datetime_str, "%Y-%m-%d_%H:%M"
        )
        end_datetime_str = json_data.get("end_datetime")
        end_datetime = None
        if end_datetime_str:
            end_datetime = datetime.strptime(
                end_datetime_str, "%Y-%m-%d_%H:%M"
            )

        status = RoundStatus[json_data.get("status")]
        round_number = json_data.get("round_number")
        serialized_games = json_data.get("games")
        games = (
            [
                self.game_serializer.deserialize(game)
                for game in serialized_games
            ]
            if serialized_games
            else []
        )

        return RoundModel(
            id=id,
            games_ids=games_ids,
            status=status,
            tournament_id=tournament_id,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            round_number=round_number,
            games=games,
        )
