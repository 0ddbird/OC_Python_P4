from tinydb import TinyDB

from models.RoundModel import RoundModel


class RoundDAO:
    db = TinyDB("./db/games.json")

    def create_player(self, player: RoundModel):
        pass

    def get_player(self, player_id):
        pass

    def update_player(self, player_id):
        pass

    def delete_player(self, player__id):
        pass
