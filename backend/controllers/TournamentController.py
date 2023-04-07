from .controller_exceptions import RoundOpenException, TournamentEndedException
from ..dao.GameDAO import GameDAO
from ..dao.PlayerDAO import PlayerDAO
from ..dao.TournamentDAO import TournamentDAO
from ..dao.RoundDAO import RoundDAO
from ..models.model_typing import ForeignKey, PrimaryKey, SerializedTournament
from ..models.TournamentModel import TournamentModel, TournamentStatus

from ..serializers.TournamentSerializer import TournamentSerializer


class TournamentController:
    def __init__(self) -> None:
        self.serializer = TournamentSerializer()
        self.tournament_dao = TournamentDAO()
        self.player_dao = PlayerDAO()
        self.round_dao = RoundDAO()
        self.game_dao = GameDAO()

    def create_tournament(
        self,
        name: str,
        location: str,
        description: str,
        players_ids: tuple[ForeignKey, ...],
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

    def get_all_tournaments(self) -> list[SerializedTournament, ...]:
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

    def update_tournament(self, tournament_id, updated_tournament) -> None:
        raise NotImplementedError

    def delete_tournament(self, tournament_id) -> None:
        raise NotImplementedError
