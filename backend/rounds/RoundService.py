from backend.games.GameDAO import GameDAO
from backend.rounds.RoundDAO import RoundDAO
from backend.tournaments.TournamentDAO import TournamentDAO
from backend.tournaments.TournamentService import TournamentService


class RoundService:
    def __init__(
        self,
        round_dao: RoundDAO,
        tournament_dao: TournamentDAO,
        game_dao: GameDAO,
        tournament_service: TournamentService,
    ):
        self.game_dao = game_dao
        self.round_dao = round_dao
        self.tournament_dao = tournament_dao
        self.tournament_service = tournament_service

    def close_round(self, round):
        round.close()
        self.round_dao.update_round(round)
        self.tournament_service.update_tournament_status(round.tournament_id)

    @staticmethod
    def are_all_games_over(games):
        for game in games:
            if not game.is_over():
                return False
        return True

    def update_round_status(self, round_id):
        round = self.round_dao.get_round(round_id)
        games_ids = round.games_ids
        games = self.game_dao.get_games_by_id(tuple(games_ids))
        if self.are_all_games_over(games):
            self.close_round(round)
