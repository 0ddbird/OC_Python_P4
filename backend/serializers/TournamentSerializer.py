from datetime import datetime

from backend.models.TournamentModel import TournamentModel


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
        creation_date = datetime.strptime(creation_date_str, "%Y-%m-%d_%H:%M")
        current_round = int(json_data.get("current_round"))
        status = json_data.get("status")

        return TournamentModel(
            name,
            max_rounds,
            location,
            description,
            players_ids,
            creation_date,
            current_round,
            status,
            t_id
        )

    @staticmethod
    def serialize(tournament):
        try:
            serialized_tournament = {
                "name": tournament.name,
                "max_rounds": tournament.max_rounds,
                "current_round": tournament.current_round,
                "location": tournament.location,
                "description": tournament.description,
                "players_ids": tournament.players_ids,
                "creation_date": tournament.creation_date.strftime("%Y-%m-%d_%H:%M"),
                "status": tournament.status
            }
            if tournament.t_id:
                serialized_tournament["tournament_id"] = tournament.t_id
            return serialized_tournament
        except Exception as e:
            print(e)



