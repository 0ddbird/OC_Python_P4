from typing import List

from ..dao.PlayerDAO import PlayerDAO
from ..dao.TournamentDAO import TournamentDAO
from ..dao.RoundDAO import RoundDAO
from ..models.TournamentModel import TournamentModel
from ..serializers.TournamentSerializer import TournamentSerializer


class MissingPlayerException(Exception):
    pass


class PlayerCountException(Exception):
    pass


class TournamentEndedException(Exception):
    def __init__(self):
        self.message = "This tournament has ended"
        super().__init__(self.message)


class TournamentController:
    def __init__(self):
        self.tournament_dao = TournamentDAO()
        self.player_dao = PlayerDAO()
        self.serializer = TournamentSerializer()
        self.round_dao = RoundDAO()

    def create_tournament(
        self,
        name: str,
        location: str,
        description: str,
        players_ids: List[int],
        max_rounds: int,
    ):
        for player_id in players_ids:
            player = self.player_dao.get_player(player_id)
            if player is None:
                raise MissingPlayerException(
                    f"Player with ID {player_id} not found"
                )

        tournament = TournamentModel(
            name,
            location,
            description,
            players_ids,
            max_rounds,
        )

        return self.tournament_dao.create_tournament(tournament)

    def get_all_tournaments(self):
        tournaments = self.tournament_dao.get_tournaments()
        serialized_tournaments = []
        for tournament in tournaments:
            serialized_tournament = self.serializer.serialize(tournament)
            serialized_tournaments.append(serialized_tournament)
        return serialized_tournaments

    def get_tournament(self, tournament_id):
        tournament = self.tournament_dao.get_tournament(tournament_id)
        return self.serializer.serialize(tournament)

    def start_tournament(self, tournament_id):
        tournament = self.tournament_dao.get_tournament(tournament_id)
        if tournament.status == "Ended":
            raise TournamentEndedException

    def update_tournament(self, tournament_id, updated_tournament):
        raise NotImplementedError

    def delete_tournament(self, tournament_id):
        raise NotImplementedError
