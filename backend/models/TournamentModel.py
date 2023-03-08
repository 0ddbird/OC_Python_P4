from datetime import datetime
from models.PlayerModel import PlayerModel
from dao.TournamentDAO import TournamentDAO


class TournamentModel:
    def __init__(self):
        self.t_id = None
        self.name = None
        self.location = None
        self.start_date = None
        self.end_date = None
        self.max_rounds = None
        self.curr_round = None
        self.players = None
        self.description = None

    def to_dict(self):
        data = asdict(self)
        data["start_date"] = self.start_date.isoformat()
        data["end_date"] = self.end_date.isoformat()
        return data

    def __str__(self):
        return (
            f"{self.name} {self.location} {self.start_date}"
            f" {self.end_date} {self.max_rounds} {self.curr_round} "
            f"{self.players} {self.description}"
        )

    def __repr__(self):
        return (
            f"{self.name} {self.location} {self.start_date}"
            f" {self.end_date} {self.max_rounds} {self.curr_round} "
            f"{self.players} {self.description}"
        )

    def create_tournament(self):
        self.dao.create_tournament(self)

    def get_tournaments(self):
        return self.dao.get_tournaments()

    def get_tournament(self, tournament_id):
        return self.dao.get_tournament(tournament_id)

    def update_tournament(self, tournament_id, updated_tournament):
        self.dao.update_tournament(tournament_id, updated_tournament)

    def delete_tournament(self, tournament_id):
        self.dao.delete_tournament(tournament_id)
