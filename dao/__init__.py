from dataclasses import asdict

from tinydb import TinyDB

from models.GameModel import GameModel


class GameDAO:
    db = TinyDB("./db/players.json")

    def create_player(self, player: GameModel):
        pass

    def get_player(self, player_id):
        pass

    def update_player(self, player_id):
        pass

    def delete_player(self, player__id):
        pass
