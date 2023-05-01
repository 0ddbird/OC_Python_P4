from datetime import datetime
from typing import Optional

from backend.abstract.typing.model_typing import SerializedTournament
from backend.rounds.serializer import RoundSerializer
from backend.tournaments.models.model import (
    TournamentModel,
    TournamentStatus,
)


class TournamentSerializer:
    def __init__(self, round_serializer=None):
        self.round_serializer: Optional[RoundSerializer] = round_serializer

    def serialize(self, tournament: TournamentModel) -> SerializedTournament:
        serialized_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "description": tournament.description,
            "players_ids": tournament.players_ids,
            "start_datetime": tournament.start_datetime.strftime(
                "%Y-%m-%d_%H:%M"
            ),
            "max_rounds": tournament.max_rounds,
            "current_round": tournament.current_round,
            "status": tournament.status.name,
            "rounds_ids": tournament.rounds_ids,
        }

        if tournament.end_datetime:
            serialized_tournament[
                "end_datetime"
            ] = tournament.end_datetime.strftime("%Y-%m-%d_%H:%M")

        if tournament.id:
            serialized_tournament["id"] = tournament.id

        if tournament.rounds:
            serialized_tournament["rounds"] = [
                self.round_serializer.serialize(round)
                for round in tournament.rounds
            ]

        return serialized_tournament

    def deserialize(self, json_data: dict) -> TournamentModel:
        id = int(json_data.get("id")) if json_data.get("id") else None
        name = json_data.get("name")
        location = json_data.get("location")
        description = json_data.get("description")
        players_ids = tuple(json_data.get("players_ids"))
        max_rounds = int(json_data.get("max_rounds"))
        start_datetime = datetime.strptime(
            json_data.get("start_datetime"), "%Y-%m-%d_%H:%M"
        )

        end_datetime_str = json_data.get("end_datetime")
        end_datetime = (
            datetime.strptime(end_datetime_str, "%Y-%m-%d_%H:%M")
            if end_datetime_str is not None
            else None
        )

        current_round = json_data.get("current_round")
        rounds_ids = json_data.get("rounds_ids")
        status = TournamentStatus[json_data.get("status")]
        rounds = json_data.get("rounds")
        deserialized_rounds = (
            [self.round_serializer.deserialize(round) for round in rounds]
            if rounds
            else []
        )

        return TournamentModel(
            name=name,
            location=location,
            description=description,
            players_ids=players_ids,
            max_rounds=max_rounds,
            rounds_ids=rounds_ids,
            current_round=current_round,
            status=status,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            id=id,
            rounds=deserialized_rounds,
        )
