from tinydb import TinyDB

from models.TournamentModel import TournamentModel


class TournamentDAO:
    db = TinyDB("./db/tournaments.json")

    def create_player(self, player: TournamentModel):
        pass

    def get_player(self, player_id):
        pass

    def update_player(self, player_id):
        pass

    def delete_player(self, player__id):
        pass
