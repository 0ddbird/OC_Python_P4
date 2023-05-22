from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedTournament,
)
from backend.games.dao import GameDAO
from backend.games.service import GameService
from backend.games.serializer import GameSerializer
from backend.players.dao import PlayerDAO
from backend.players.serializer import PlayerSerializer
from backend.rounds.dao import RoundDAO
from backend.rounds.service import RoundService
from backend.rounds.serializer import RoundSerializer
from backend.tournaments.dao import TournamentDAO
from backend.tournaments.model import TournamentModel
from backend.tournaments.serializer import TournamentSerializer


class TournamentService:
    def __init__(self):
        self.tournament_dao: TournamentDAO = TournamentDAO()
        self.round_dao: RoundDAO = RoundDAO()
        self.game_dao: GameDAO = GameDAO()
        self.player_dao = PlayerDAO()
        self.round_service: RoundService = RoundService()
        self.game_service: GameService = GameService()
        self.player_serializer: PlayerSerializer = PlayerSerializer()
        self.game_serializer: GameSerializer = GameSerializer()
        self.round_serializer: RoundSerializer = RoundSerializer(
            game_serializer=self.game_serializer
        )
        self.serializer: TournamentSerializer = TournamentSerializer(
            round_serializer=self.round_serializer,
            player_serializer=self.player_serializer,
        )

    def create_tournament(
            self,
            name: str,
            location: str,
            description: str,
            players_ids: tuple[ForeignKey],
            max_rounds: int,
    ) -> PrimaryKey:
        for player_id in players_ids:
            self.player_dao.get(player_id)
        tournament = TournamentModel(
            name=name,
            location=location,
            description=description,
            players_ids=players_ids,
            max_rounds=max_rounds,
        )
        return self.tournament_dao.create(tournament)

    def get_tournament(
            self, tournament_id, players=False, rounds=False
    ) -> SerializedTournament:
        tournament = self.tournament_dao.get(tournament_id)
        if rounds is True:
            self.set_tournament_round(tournament)
        if players is True:
            self.set_tournament_players(tournament)
        return self.serializer.serialize(tournament)

    def get_all_tournaments(self, rounds=False) -> list[SerializedTournament]:
        tournaments = self.tournament_dao.get_all()
        if rounds:
            for tournament in tournaments:
                self.set_tournament_round(tournament)

        return [
            self.serializer.serialize(tournament) for tournament in tournaments
        ]

    def set_tournament_round(self, tournament: TournamentModel) -> None:
        rounds = self.round_service.get_tournament_rounds(
            tournament.rounds_ids, games=True
        )
        if rounds:
            tournament.set_rounds(rounds)

    def set_tournament_players(self, tournament: TournamentModel) -> None:
        tournament.players = self.player_dao.get_multiple(
            tournament.players_ids
        )

    def get_round_id(self, tournament_id, round_number):
        tournament = self.tournament_dao.get(tournament_id)
        round_id = tournament.rounds_ids[round_number - 1]
        return round_id

    def create_round(self, tournament_id: PrimaryKey) -> None:
        serialized_tournament = self.get_tournament(
            tournament_id, rounds=False, players=False
        )
        tournament = self.serializer.deserialize(serialized_tournament)

        player_pairs = tournament.pair_players()
        games_ids = self.game_service.create_multiple_games(
            player_pairs, tournament_id
        )
        round_id = self.round_service.create_round(
            games_ids, tournament.id, tournament.current_round + 1
        )
        self.game_service.update_games_ids(games_ids, round_id)
        current_rounds_ids = list(tournament.rounds_ids)
        current_rounds_ids.append(round_id)
        tournament.set_rounds_ids(tuple(current_rounds_ids))
        tournament.set_status_open()
        self.tournament_dao.update(tournament)

    def close_tournament(self, tournament_id: PrimaryKey):
        tournament = self.tournament_dao.get(tournament_id)
        tournament.set_status_started()
        self.tournament_dao.update(tournament)

    def close_round(self, tournament_id: PrimaryKey):
        tournament = self.tournament_dao.get(tournament_id)
        tournament.set_status_started()
        self.tournament_dao.update(tournament)

    def update_game_results(self, game_id: PrimaryKey, p1_score: float):
        game = self.game_dao.get(game_id)
        game.set_results(p1_score)
        self.game_service.update_game(game)

        serialized_round = self.round_service.get_round(
            game.round_id, games=True
        )
        serialized_tournament = self.get_tournament(
            game.tournament_id, rounds=True
        )
        round = self.round_serializer.deserialize(serialized_round)
        tournament = self.serializer.deserialize(serialized_tournament)

        if round.is_over():
            round.end()
            self.round_dao.update(round)
            if tournament.has_remaining_rounds():
                tournament.set_status_started()
            else:
                tournament.end()
            self.tournament_dao.update(tournament)
