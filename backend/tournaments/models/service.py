from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedTournament,
)
from backend.games.dao import GameDAO
from backend.games.models.GameModel import GameModel
from backend.games.models.GameService import GameService
from backend.games.serializer import GameSerializer
from backend.players.dao import PlayerDAO
from backend.rounds.dao import RoundDAO
from backend.rounds.models.service import RoundService
from backend.rounds.serializer import RoundSerializer
from backend.tournaments.dao import TournamentDAO
from backend.tournaments.models.model import TournamentModel
from backend.tournaments.serializer import TournamentSerializer
from backend.tournaments.utils import (
    get_opponents_history,
    rank_players,
)


class TournamentService:
    def __init__(self):
        self.dao: TournamentDAO = TournamentDAO()
        self.round_dao: RoundDAO = RoundDAO()
        self.game_dao: GameDAO = GameDAO()
        self.player_dao = PlayerDAO()
        self.round_service: RoundService = RoundService()
        self.game_service: GameService = GameService()
        self.game_serializer: GameSerializer = GameSerializer()
        self.round_serializer: RoundSerializer = RoundSerializer(
            game_serializer=self.game_serializer
        )
        self.serializer: TournamentSerializer = TournamentSerializer(
            round_serializer=self.round_serializer
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
        return self.dao.create(tournament)

    def get_tournament(
        self, tournament_id, eager=False
    ) -> SerializedTournament:
        tournament = self.dao.get(tournament_id)
        if eager:
            self.set_tournament_round(tournament)

        return self.serializer.serialize(tournament)

    def get_all_tournaments(self, eager=False) -> list[SerializedTournament]:
        tournaments = self.dao.get_all()
        if eager:
            for tournament in tournaments:
                self.set_tournament_round(tournament)

        return [
            self.serializer.serialize(tournament) for tournament in tournaments
        ]

    def set_tournament_round(self, tournament: TournamentModel) -> None:
        rounds = self.round_service.get_tournament_rounds(
            tournament.rounds_ids, eager=True
        )
        tournament.set_rounds(rounds)

    def get_round_id(self, tournament_id, round_number):
        tournament = self.dao.get(tournament_id)
        round_id = tournament.rounds_ids[round_number - 1]
        return round_id

    def create_round(self, tournament_id: PrimaryKey) -> None:
        serialized_tournament = self.get_tournament(tournament_id, eager=False)
        tournament = self.serializer.deserialize(serialized_tournament)

        player_pairs = tournament.pair_players()
        games_ids = self.game_service.create_multiple_games(player_pairs)
        round_id = self.round_service.create_round(
            games_ids, tournament.id, tournament.current_round + 1
        )
        self.game_service.update_games_ids(games_ids, round_id)

        # Append Tournament.rounds_ids
        current_rounds_ids = list(tournament.rounds_ids)
        current_rounds_ids.append(round_id)
        tournament.set_rounds_ids(tuple(current_rounds_ids))

        # Set Tournament status to ROUND_OPEN
        tournament.set_round_open()
        self.dao.update(tournament_id, tournament)

    def close_tournament(self, tournament_id: PrimaryKey):
        tournament = self.dao.get(tournament_id)
        tournament.set_status_started()
        self.dao.update(
            id=tournament_id,
            tournament=tournament,
        )

    def close_round(self, tournament_id: PrimaryKey):
        tournament = self.dao.get(tournament_id)
        tournament.set_status_started()
        self.dao.update(tournament_id, tournament)

    def get_tournament_snapshot(self, tournament: TournamentModel):
        rounds = self.round_dao.get_multiple_rounds(tournament.rounds_ids)
        games_ids = [round.games_ids for round in rounds]
        games = self.game_dao.get_multiple(tuple(*games_ids))
        return [game.get_player_results() for game in games]

    def matchmake_players(self, tournament: TournamentModel):
        tournament_snapshot = self.get_tournament_snapshot(tournament)
        ranking = rank_players(tournament_snapshot)
        history = get_opponents_history(tournament_snapshot)
        return generate_pairings(ranking, history)

    def update_game_results(self, game_id, p1_score, p2_score):
        """
        Update a Game object by setting the player scores
        After updating the game, update the round to change its status if
        all games have the status GameStatus.OVER
        """

        game = self.game_dao.get(game_id)
        game.set_players_score(p1_score, p2_score)
        self.game_dao.update(game)

        # If all games of the related round have the status == GameStatus.OVER
        # Update the round status to RoundStatus.OVER
        round = self.round_dao.get(game.round_id)
        round_games = self.game_dao.get_multiple(round.games_ids)
        print(f"Games IDS for round {round.games_ids}")
        if self.all_games_over(round_games):
            print("AppService\n" f"All games for round {round.id} are over")
            self.round_service.close_round(round)
            self.close_round(round.tournament_id)

    @staticmethod
    def all_games_over(games: list[GameModel]):
        for game in games:
            if not game.is_over():
                return False
        return True
