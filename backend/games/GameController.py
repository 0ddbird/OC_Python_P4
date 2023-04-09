from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedGame,
)
from backend.games.GameDAO import GameDAO
from backend.games.GameModel import GameModel
from backend.games.GameSerializer import GameSerializer


class GameController:
    def __init__(self):
        self.dao = GameDAO()
        self.serializer = GameSerializer()

    def get_game(self, game_id: PrimaryKey) -> SerializedGame:
        game = self.dao.get_game(game_id)
        return self.serializer.serialize(game)

    def get_all_games(self) -> list[SerializedGame]:
        games = self.dao.get_all_games()
        return [self.serializer.serialize(game) for game in games]

    def create_game(self, p1_id: ForeignKey, p2_id: ForeignKey) -> PrimaryKey:
        game = GameModel(
            p1_id=p1_id,
            p2_id=p2_id,
        )
        return self.dao.create_game(game)

    def update_game(self, game_id, request) -> None:
        p1_score = request.json.get("p1_score")
        p2_score = request.json.get("p2_score")
        game = self.dao.get_game(game_id)
        game.set_p1_score(p1_score)
        game.set_p2_score(p2_score)
        self.dao.update_game(game)

    def get_games_by_id(
        self, games_ids: list[PrimaryKey]
    ) -> list[SerializedGame]:
        games = self.dao.get_games_by_id(tuple(games_ids))
        return [self.serializer.serialize(game) for game in games]
