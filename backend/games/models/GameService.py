from typing import Iterable

from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey
from backend.games.dao import GameDAO
from backend.games.models.GameModel import GameModel


class GameService:
    def __init__(self):
        self.dao: GameDAO = GameDAO()

    def create_game(self, p1_id, p2_id) -> PrimaryKey:
        game = GameModel(
            p1_id=p1_id,
            p2_id=p2_id,
        )
        return self.dao.create(game)

    def create_multiple_games(
        self,
        pairs: tuple[tuple[ForeignKey, ForeignKey], ...],
    ) -> list[PrimaryKey]:
        games_ids = []
        for pair in pairs:
            player_1, player_2 = pair[0], pair[1]
            game_id = self.create_game(player_1, player_2)
            games_ids.append(game_id)
        return games_ids

    def update_games_ids(
        self,
        games_ids: Iterable[PrimaryKey],
        round_id: PrimaryKey,
    ) -> None:
        games = self.dao.get_multiple(games_ids)
        for game in games:
            game.set_round_id(round_id)
            self.dao.update(game)
