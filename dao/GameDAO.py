import os

from tinydb import TinyDB, Query

from models.GameModel import GameModel


class GameDAO:
    db = TinyDB(os.path.join(os.getcwd(), "db", "games.json"))

    def create_game(self, game: GameModel):
        game_dict = game.to_dict()
        self.db.insert(game_dict)

    def get_games(self):
        return self.db.all()

    def get_game(self, game_id):
        user = Query()
        return self.db.search(user.p_id.matches(game_id))
