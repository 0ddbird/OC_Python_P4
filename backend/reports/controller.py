from backend.players.service import PlayerService
from backend.tournaments.service import TournamentService


class ReportController:
    def __init__(self):
        self.player_service = PlayerService()
        self.tournament_service = TournamentService()

    def get_reports(self):
        raise NotImplementedError

    def get_players(self):
        return self.player_service.get_all_players()

    def post_players(self):
        return self.player_service.get_all_players()

    def get_tournaments(self):
        return self.tournament_service.get_all_tournaments(rounds=False)

    def post_tournaments(self):
        return self.tournament_service.get_all_tournaments(rounds=False)

    def get_tournament(self, tournament_id, base, players, rounds):
        return self.tournament_service.get_all_tournaments(rounds=rounds)

    def post_tournament(self, tournament_id, base, players, rounds):
        return self.tournament_service.get_all_tournaments(rounds=rounds)
