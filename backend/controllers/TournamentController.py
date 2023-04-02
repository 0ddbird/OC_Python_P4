from datetime import (
    datetime,
)
from typing import (
    List,
)

from ..dao.PlayerDAO import (
    PlayerDAO,
)
from ..dao.TournamentDAO import (
    TournamentDAO,
)
from ..models.TournamentModel import (
    TournamentModel,
)
from ..serializers.TournamentSerializer import (
    TournamentSerializer,
)


class MissingPlayerException(Exception):
    pass


class PlayerCountException(Exception):
    pass


class TournamentNotFoundException(Exception):
    pass


class TournamentController:
    def __init__(self):
        self.tournament_dao = TournamentDAO()
        self.player_dao = PlayerDAO()
        self.serializer = TournamentSerializer()

    def create_tournament(
        self,
        name,
        max_rounds,
        location,
        description,
        players_ids: List[int],
    ):
        for player_id in players_ids:
            player = self.player_dao.get_player(player_id)
            if player is None:
                raise MissingPlayerException(
                    f"Player with ID {player_id} not found"
                )

        creation_datetime = datetime.now()
        current_round = 0
        status = "To start"
        tournament = TournamentModel(
            name,
            max_rounds,
            location,
            description,
            players_ids,
            creation_datetime,
            current_round,
            status,
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
        try:
            tournament = self.tournament_dao.get_tournament(tournament_id)
            serialized_tournament = self.serializer.serialize(tournament)
            return serialized_tournament
        except Exception as e:
            raise TournamentNotFoundException(
                f"Tournament with ID " f"{tournament_id} not found, {e}"
            )

    def update_tournament(self, tournament_id, updated_tournament):
        raise NotImplementedError

    def delete_tournament(self, tournament_id):
        raise NotImplementedError
