from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedGame,
)
from backend.games.GameDAO import GameDAO
from backend.games.GameModel import GameModel
from backend.games.GameSerializer import GameSerializer
from backend.games.GameService import GameService
from backend.rounds.RoundDAO import RoundDAO
from backend.rounds.RoundService import RoundService
from backend.tournaments.TournamentDAO import TournamentDAO
from backend.tournaments.TournamentService import TournamentService


class GameController:
    def __init__(self):
        self.game_dao = GameDAO()
        self.round_dao = RoundDAO()
        self.tournament_dao = TournamentDAO()
        self.serializer = GameSerializer()
        self.tournament_service = TournamentService(
            tournament_dao=self.tournament_dao,
            game_dao=self.game_dao,
            round_dao=self.round_dao,
        )
        self.round_service = RoundService(
            round_dao=self.round_dao,
            tournament_dao=self.tournament_dao,
        )
        self.game_service = GameService(
            game_dao=self.game_dao,
            round_dao=self.round_dao,
            round_service=self.round_service,
        )

    def get_game(self, game_id: PrimaryKey) -> SerializedGame:
        game = self.game_dao.get_game(game_id)
        return self.serializer.serialize(game)

    def get_all_games(self) -> list[SerializedGame]:
        games = self.game_dao.get_all_games()
        return [self.serializer.serialize(game) for game in games]

    def create_game(self, p1_id: ForeignKey, p2_id: ForeignKey) -> PrimaryKey:
        game = GameModel(
            p1_id=p1_id,
            p2_id=p2_id,
        )
        return self.game_dao.create_game(game)

    def update_game(self, game_id, p1_score, p2_score) -> None:
        game = self.game_dao.get_game(game_id)
        self.game_service.set_players_score(game, p1_score, p2_score)

    def get_games_by_id(
        self, games_ids: list[PrimaryKey]
    ) -> list[SerializedGame]:
        games = self.game_dao.get_games_by_id(tuple(games_ids))
        return [self.serializer.serialize(game) for game in games]
