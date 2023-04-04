import os
from tinydb import TinyDB, Query
from backend.models.GameModel import GameModel
from backend.serializers.GameSerializer import GameSerializer


class GameDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "games.json"))
        self.serializer = GameSerializer()

    def create_game(self, game: GameModel):
        serialized_game = self.serializer.serialize_to_db(game)
        return self.db.insert(serialized_game)

    def get_games(self):
        return self.db.all()

    def get_game(self, game_id):
        game_record = self.db.get(doc_id=game_id)
        return self.serializer.deserialize(game_record)

    def get_games_by_ids(self, game_ids):
        games = []
        for game_id in game_ids:
            game = self.get_game(game_id)
            games.append(game)
        return games

    def update_game(self, updated_game: GameModel):
        serialized_game = self.serializer.serialize_to_db(updated_game)
        return self.db.update(serialized_game, doc_ids=[updated_game.g_id])

    def delete_game(self, game_id):
        user = Query()
        self.db.remove(user.p_id.matches(game_id))
