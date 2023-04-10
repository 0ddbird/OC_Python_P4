from backend.abstract.typing.model_typing import ForeignKey, PrimaryKey
from backend.games.GameModel import GameModel
from backend.rounds.RoundModel import RoundModel
from backend.tournaments.TournamentModel import (
    TournamentModel,
    TournamentStatus,
)
from backend.tournaments.utils import shuffle_players, sort_by_score


class TournamentService:
    def __init__(self, tournament_dao, game_dao, round_dao):
        self.tournament_dao = tournament_dao
        self.game_dao = game_dao
        self.round_dao = round_dao

    def update_tournament_status(self, tournament_id):
        tournament = self.tournament_dao.get_tournament(tournament_id)
        tournament.close_round()
        self.tournament_dao.update_tournament(
            tournament_id=tournament_id,
            tournament=tournament,
        )

    def create_game(self, p1_id, p2_id) -> PrimaryKey:
        game = GameModel(p1_id=p1_id, p2_id=p2_id)
        return self.game_dao.create_game(game)

    def create_multiple_games(
        self, p_ids: tuple[PrimaryKey]
    ) -> tuple[PrimaryKey]:
        games_ids = []
        for i in range(0, len(p_ids), 2):
            p1_id, p2_id = p_ids[i], p_ids[i + 1]
            game_id = self.create_game(p1_id, p2_id)
            games_ids.append(game_id)
        return tuple(games_ids)

    def create_round(
        self,
        games_ids: tuple[PrimaryKey],
        tournament_id: ForeignKey,
        round_number: int,
    ) -> PrimaryKey:
        round = RoundModel(
            games_ids=games_ids,
            tournament_id=tournament_id,
            round_number=round_number,
        )
        return self.round_dao.create_round(round)

    def update_games(
        self, games_ids: tuple[PrimaryKey], round_id: PrimaryKey
    ) -> None:
        games = self.game_dao.get_games_by_id(games_ids)

        for game in games:
            game.set_round_id(round_id)
            self.game_dao.update_game(game)

    def create_next_round(self, tournament: TournamentModel) -> ForeignKey:
        players_ids = list(tournament.players_ids)
        players_pairs = []

        # CASE 1: first round
        if tournament.status == TournamentStatus.TO_START:
            players_pairs = shuffle_players(players_ids)

        # CASE 2: next rounds
        if tournament.status == TournamentStatus.STARTED:
            players_pairs = sort_by_score(players_ids)

        # Create games based on players pairs
        games_ids = self.create_multiple_games(tuple(players_pairs))

        # Create round based on the games IDs
        round_id = self.create_round(
            games_ids, tournament.id, tournament.current_round + 1
        )

        # Insert the Round ID into each Game record
        self.update_games(games_ids, round_id)

        # Append Tournament.rounds_ids
        current_rounds_ids = list(tournament.rounds_ids)

        current_rounds_ids.append(round_id)
        tournament.rounds_ids = tuple(current_rounds_ids)

        # Set Tournament status to ROUND_OPEN
        tournament.status = TournamentStatus.ROUND_OPEN

        # Set Tournament currentRound
        tournament.current_round += 1

        return round_id
