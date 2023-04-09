from flask import Request

from backend.games.GameDAO import GameDAO
from backend.rounds.RoundDAO import RoundDAO
from backend.tournaments.TournamentDAO import TournamentDAO
from backend.abstract.typing.model_typing import PrimaryKey, SerializedRound
from backend.rounds.RoundSerializer import RoundSerializer


class RoundController:
    def __init__(self) -> None:
        self.dao: RoundDAO = RoundDAO()
        self.tournamentDAO: TournamentDAO = TournamentDAO()
        self.serializer: RoundSerializer = RoundSerializer()
        self.gameDAO: GameDAO = GameDAO()

    def get_round(self, id: PrimaryKey) -> SerializedRound:
        round = self.dao.get_round(id)
        return self.serializer.serialize(round)

    def get_all_rounds(self) -> list[SerializedRound]:
        rounds = self.dao.get_all_rounds()
        return [self.serializer.serialize(round) for round in rounds]

    def update_round(self, id: PrimaryKey, http_request: Request) -> None:
        round = self.get_round(id)
        self.dao.update_round(round)

    def update_all_round_games(
        self, round_id: PrimaryKey, request: Request
    ) -> None:
        round = self.dao.get_round(round_id)
        games = request.json.get("games")
        print(round, games)
        # game_ids = {game['game_id'] for game in games}
        # if set(round.games_ids) != game_ids:
        #     raise ValueError(
        #         "Provided game IDs do not match the round's game IDs.")
        # print(round, games, game_ids)
        # for game_data in games:
        #     game = self.gameDAO.get_game(game_data['game_id'])
        #     game.set_p1_score(game_data['p1_score'])
        #     game.set_p2_score(game_data['p2_score'])
        #
        # self.dao.update_round(round)
        # round.close()
        # tournament = self.tournamentDAO.get_tournament(round.tournament_id)
        # tournament.close_round()
        # self.tournamentDAO.update_tournament(tournament)
