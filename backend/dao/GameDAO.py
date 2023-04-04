import os
from tinydb import TinyDB, Query
from backend.models.GameModel import GameModel


class GameDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "games.json"))

    def create_game(self, game: GameModel):
        game_dict = game.to_dict()
        self.db.insert(game_dict)

    def get_games(self):
        return self.db.all()

    def get_game(self, game_id):
        user = Query()
        return self.db.search(user.p_id.matches(game_id))

    def update_game(self, game_id, updated_game):
        user = Query()
        self.db.update(updated_game, user.p_id.matches(game_id))

    def delete_game(self, game_id):
        user = Query()
        self.db.remove(user.p_id.matches(game_id))
