from datetime import datetime


class TournamentModel:
    def __init__(
        self,
        name,
        location,
        description,
        players_ids,
        max_rounds=4,
        creation_date=datetime.now(),
        current_round=0,
        status="To start",
        rounds=[],
        t_id=None,
    ):
        self.t_id = t_id
        self.name = name
        self.max_rounds = max_rounds
        self.location = location
        self.description = description
        self.players_ids = players_ids
        self.creation_date = creation_date
        self.current_round = current_round
        self.end_date = None
        self.status = status
        self.rounds = rounds
