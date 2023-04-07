from datetime import datetime

from backend.models.model_typing import SerializedTournament
from backend.models.TournamentModel import TournamentModel, TournamentStatus


class TournamentSerializer:
    @staticmethod
    def serialize(tournament: TournamentModel) -> SerializedTournament:
        serialized_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "description": tournament.description,
            "players_ids": tournament.players_ids,
            "start_datetime": tournament.start_datetime.strftime(
                "%Y-%m-%d_%H:%M"
            ),
            "end_datetime": tournament.end_datetime.strftime("%Y-%m-%d_%H:%M")
            if tournament.end_datetime
            else None,
            "max_rounds": tournament.max_rounds,
            "current_round": tournament.current_round,
            "status": tournament.status.name,
            "rounds_ids": tournament.rounds_ids,
        }

        if tournament.id:
            serialized_tournament["id"] = tournament.id
        return serialized_tournament

    @staticmethod
    def deserialize(json_data: dict) -> TournamentModel:
        id = int(json_data.get("id"))
        name = json_data.get("name")
        location = json_data.get("location")
        description = json_data.get("description")
        players_ids = tuple(json_data.get("players_ids"))
        max_rounds = int(json_data.get("max_rounds"))
        start_datetime_str = json_data.get("start_datetime")
        start_datetime = datetime.strptime(
            start_datetime_str,
            "%Y-%m-%d_%H:%M",
        )
        end_datetime_str = json_data.get("end_datetime")

        end_datetime = (
            datetime.strptime(
                end_datetime_str,
                "%Y-%m-%d_%H:%M",
            )
            if end_datetime_str is not None
            else None
        )
        current_round = json_data.get("current_round")
        rounds_ids = json_data.get("rounds_ids")
        status = TournamentStatus[json_data.get("status")]

        return TournamentModel(
            name=name,
            location=location,
            description=description,
            players_ids=players_ids,
            max_rounds=max_rounds,
            start_datetime=start_datetime,
            end_datetime=end_datetime,
            current_round=current_round,
            status=status,
            rounds_ids=rounds_ids,
            id=id,
        )
