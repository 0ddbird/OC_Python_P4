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

    def __repr__(self):
        return f"TournamentModel({self.t_id}, {self.name}, {self.max_rounds}, {self.location}, {self.description}, {self.players_ids}, {self.creation_date}, {self.current_round}, {self.end_date}, {self.status}, {self.rounds})"

    def __str__(self):
        return (
            f"TournamentModel\n"
            f"{self.t_id=}\n"
            f"{self.name=}\n"
            f"{self.max_rounds=}\n"
            f"{self.location=}\n"
            f"{self.description=}\n"
            f"{self.players_ids=}\n"
            f"{self.creation_date=}\n"
            f"{self.current_round=}\n"
            f"{self.end_date=}\n"
            f"{self.status=}\n"
            f"{self.rounds=}\n"
        )

    def set_to_next_round(self):
        self.current_round += 1
