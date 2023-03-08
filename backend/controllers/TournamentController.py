from models.TournamentModel import TournamentModel

class TournamentController:

    def __init__(self):
        self.tournament = TournamentModel()

    def create_tournament(self):
        self.tournament.create_tournament()

    def get_tournaments(self):
        return self.tournament.get_tournaments()

    def get_tournament(self, tournament_id):
        return self.tournament.get_tournament(tournament_id)

    def update_tournament(self, tournament_id, updated_tournament):
        self.tournament.update_tournament(tournament_id, updated_tournament)

    def delete_tournament(self, tournament_id):
        self.tournament.delete_tournament(tournament_id)