import os

from tinydb import TinyDB
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
        try:
            del serialized_game["id"]
        except KeyError:
            pass
        return self.table.insert(serialized_game)

    def get_game(self, game_id: PrimaryKey) -> GameModel:
        game_record = self.table.get(doc_id=game_id)
        game_record["id"] = game_id
        return self.serializer.deserialize(game_record)

    def get_all_games(self) -> list[GameModel]:
        records = self.table.all()
        for record in records:
            record["id"] = record.doc_id
        return [self.serializer.deserialize(record) for record in records]

    def get_games_by_id(self, game_ids: tuple[PrimaryKey]):
        games = []
        for game_id in game_ids:
            game = self.get_game(game_id)
            games.append(game)
        return games

    def update_game(self, updated_game: GameModel):
        serialized_game = self.serializer.serialize(updated_game)
        return self.table.update(serialized_game, doc_ids=[updated_game.id])

    def delete_game(self, game_id: PrimaryKey) -> None:
        self.table.remove(doc_ids=[game_id])
