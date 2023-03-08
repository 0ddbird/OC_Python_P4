import os
from tinydb import TinyDB, Query
from models.TournamentModel import TournamentModel


class TournamentDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "tournaments.json"))

    def create_tournament(self, tournament: TournamentModel):
        tournament_dict = tournament.to_dict()
        self.db.insert(tournament_dict)

    def get_tournaments(self):
        return self.db.all()

    def get_tournament(self, tournament_id):
        return self.db.search(Query().t_id.matches(tournament_id))

    def update_tournament(self, tournament_id, updated_tournament):
        tournament = Query()
        self.db.update(
            updated_tournament, tournament.t_id.matches(tournament_id)
        )

    def delete_tournament(self, tournament_id):
        tournament = Query()
        self.db.remove(tournament.t_id.matches(tournament_id))
