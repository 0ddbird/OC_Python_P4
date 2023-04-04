from datetime import (
    datetime,
)

from backend.models.TournamentModel import (
    TournamentModel,
)


class TournamentSerializer:
    def __init__(self):
        pass

    @staticmethod
    def deserialize(json_data):
        t_id = int(json_data.get("tournament_id")) or None
        name = json_data.get("name")
        max_rounds = int(json_data.get("max_rounds"))
        location = json_data.get("location")
        description = json_data.get("description")
        players_ids = json_data.get("players_ids")
        creation_date_str = json_data.get("creation_date")
        creation_date = datetime.strptime(
            creation_date_str,
            "%Y-%m-%d_%H:%M",
        )
        current_round = int(json_data.get("current_round"))
        rounds = json_data.get("rounds")
        status = json_data.get("status")

        return TournamentModel(
            name,
            location,
            description,
            players_ids,
            max_rounds,
            creation_date,
            current_round,
            status,
            rounds,
            t_id,
        )

    @staticmethod
    def serialize(tournament):
        serialized_tournament = {
            "name": tournament.name,
            "location": tournament.location,
            "description": tournament.description,
            "players_ids": tournament.players_ids,
            "creation_date": tournament.creation_date.strftime(
                "%Y-%m-%d_%H:%M"
            ),
            "max_rounds": tournament.max_rounds,
            "current_round": tournament.current_round,
            "status": tournament.status,
            "rounds": tournament.rounds,
        }
        if tournament.t_id:
            serialized_tournament["tournament_id"] = tournament.t_id
        return serialized_tournament
