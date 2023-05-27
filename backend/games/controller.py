from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedGame,
)
from backend.games.dao import GameDAO
from backend.games.service import GameService
from backend.games.serializer import GameSerializer
from backend.rounds.dao import RoundDAO
from backend.tournaments.dao import TournamentDAO
from backend.tournaments.service import TournamentService


class GameController:
    def __init__(self):
        self.serializer = GameSerializer()
        self.game_dao = GameDAO()
        self.round_dao = RoundDAO()
        self.tournament_dao = TournamentDAO()
        self.service = GameService()
        self.tournament_service = TournamentService()

    def get(self, game_id: PrimaryKey) -> SerializedGame:
        game = self.game_dao.get(game_id)
        return self.serializer.serialize(game)

    def get_multiple(self, games_ids: list[PrimaryKey]) -> list[SerializedGame]:
        games = self.game_dao.get_multiple(tuple(games_ids))
        return [self.serializer.serialize(game) for game in games]

    def get_all(self) -> list[SerializedGame]:
        games = self.game_dao.get_all()
        return [self.serializer.serialize(game) for game in games]

    def create(self, p1_id: ForeignKey, p2_id: ForeignKey) -> PrimaryKey:
        return self.service.create_game(p1_id, p2_id)

    def update(self, game_id, p1_score) -> None:
        self.tournament_service.update_game_results(game_id, p1_score)
