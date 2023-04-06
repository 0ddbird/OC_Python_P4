import os
from typing import List

from tinydb import TinyDB, Query
from backend.models.GameModel import GameModel
from backend.models.model_typing import PrimaryKey
from backend.serializers.GameSerializer import GameSerializer


class GameDAO:
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("games")
        self.serializer = GameSerializer()

    def create_game(self, game: GameModel) -> PrimaryKey:
        serialized_game = self.serializer.serialize(game)
        del serialized_game["id"]
        return self.table.insert(serialized_game)

    def get_games(self):
        return self.table.all()

    def get_game(self, game_id: PrimaryKey) -> GameModel:
        game_record = self.table.get(doc_id=game_id)
        return self.serializer.deserialize(game_record)

    def get_games_by_ids(self, game_ids: List[PrimaryKey]):
        games = []
        for game_id in game_ids:
            game = self.get_game(game_id)
            games.append(game)
        return games

    def update_game(self, updated_game: GameModel):
        serialized_game = self.serializer.serialize(updated_game)
        return self.table.update(serialized_game, doc_ids=[updated_game.id])

    def delete_game(self, game_id: PrimaryKey):
        user = Query()
        self.table.remove(user.p_id.matches(game_id))
