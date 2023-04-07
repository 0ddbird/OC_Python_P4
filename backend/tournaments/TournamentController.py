from backend.abstract.exceptions.controller_exceptions import (
    RoundOpenException,
    TournamentEndedException,
)
from backend.games.GameDAO import GameDAO
from backend.players.PlayerDAO import PlayerDAO
from backend.tournaments.TournamentDAO import TournamentDAO
from backend.rounds.RoundDAO import RoundDAO
from backend.games.GameModel import GameModel
from backend.abstract.typing.model_typing import (
    ForeignKey,
    PrimaryKey,
    SerializedRound,
    SerializedTournament,
)
from backend.tournaments.TournamentModel import (
    TournamentModel,
    TournamentStatus,
)
from backend.games.GameSerializer import GameSerializer
from backend.rounds.RoundSerializer import RoundSerializer

from backend.tournaments.TournamentSerializer import TournamentSerializer


class TournamentController:
    def __init__(self) -> None:
        self.serializer = TournamentSerializer()
        self.round_serializer = RoundSerializer()
        self.game_serializer = GameSerializer()
        self.tournament_dao = TournamentDAO()
        self.player_dao = PlayerDAO()
        self.round_dao = RoundDAO()
        self.game_dao = GameDAO()

    def create_tournament(
        self,
        name: str,
        location: str,
        description: str,
        players_ids: tuple[ForeignKey],
        max_rounds: int,
    ) -> PrimaryKey:
        for player_id in players_ids:
            self.player_dao.get_player(player_id)

        tournament = TournamentModel(
            name=name,
            location=location,
            description=description,
            players_ids=players_ids,
            max_rounds=max_rounds,
        )
        return self.tournament_dao.create_tournament(tournament)

    def get_all_tournaments(self) -> list[SerializedTournament]:
        tournaments = self.tournament_dao.get_tournaments()
        serialized_tournaments = []
        for tournament in tournaments:
            serialized_tournament = self.serializer.serialize(tournament)
            serialized_tournaments.append(serialized_tournament)
        return serialized_tournaments

    def get_tournament(self, tournament_id) -> SerializedTournament:
        tournament = self.tournament_dao.get_tournament(tournament_id)
        return self.serializer.serialize(tournament)

    def create_next_round(self, tournament_id) -> ForeignKey:
        tournament = self.tournament_dao.get_tournament(tournament_id)

        if tournament.status == TournamentStatus.ENDED:
            raise TournamentEndedException

        if tournament.status == TournamentStatus.ROUND_OPEN:
            raise RoundOpenException

        round_id = tournament.create_next_round()
        self.tournament_dao.update_tournament(
            tournament_id=tournament.id,
            updated_tournament=tournament,
        )
        return round_id

    def get_tournament_rounds(
        self,
        tournament_id: PrimaryKey,
    ) -> dict:
        tournament = self.tournament_dao.get_tournament(tournament_id)
        rounds_ids = tournament.rounds_ids
        rounds = self.round_dao.get_rounds_by_id(rounds_ids)
        round_games = {}

        for round in rounds:
            games_ids = round.games_ids
            games = self.game_dao.get_games_by_id(games_ids)
            serialized_games = [
                self.game_serializer.serialize(game) for game in games
            ]
            round_games[round.id] = serialized_games

        payload = {
            "rounds": [
                self.round_serializer.serialize(round) for round in rounds
            ],
            "games": round_games,
        }
        return payload

    def get_round_id(
        self, tournament_id: PrimaryKey, round_number
    ) -> ForeignKey:
        tournament = self.tournament_dao.get_tournament(tournament_id)
        return tournament.rounds_ids[round_number - 1]

    def get_game_ids(self, round_id: PrimaryKey) -> tuple[ForeignKey]:
        round = self.round_dao.get_round(round_id)
        return round.games_ids

    def get_game(self, game_id: PrimaryKey) -> GameModel:
        return self.game_dao.get_game(game_id)

    def get_rounds_games(self, r_id: PrimaryKey) -> list[GameModel]:
        g_ids = self.get_game_ids(r_id)
        return [self.get_game(g_id) for g_id in g_ids]

    def get_tournament_round(
        self,
        tournament_id: PrimaryKey,
        round_number: int,
    ) -> SerializedRound:
        # Find round based on round number in Tournament
        r_id = self.get_round_id(tournament_id, round_number)
        round = self.round_dao.get_round(r_id)

        # Serialize RoundModel instance
        serialized_round = self.round_serializer.serialize(round)

        # Append serialized GameModel instances to SerializedRound
        round_games = self.get_rounds_games(r_id)
        serialized_games = [
            self.game_serializer.serialize(game) for game in round_games
        ]
        serialized_round["games"] = serialized_games

        return serialized_round

    def update_games(
        self, tournament_id: PrimaryKey, round_number: int, games_dict: dict
    ) -> None:
        tournament = self.tournament_dao.get_tournament(tournament_id)
        round_id = tournament.rounds_ids[round_number - 1]
        round_games = self.get_rounds_games(round_id)

        for game in round_games:
            # Find game from games_data
            game_data = games_dict.get(game.id)

            # Unpack player scores from games_data
            p1_score = game_data.get("p1_score")
            p2_score = game_data.get("p2_score")

            # Update GameModel with new fields
            # Save GameModel to DB

        return None

    def update_tournament(self, tournament_id, updated_tournament) -> None:
        raise NotImplementedError

    def delete_tournament(self, tournament_id) -> None:
        raise NotImplementedError
