from typing import List
from datetime import datetime
from ..models.TournamentModel import TournamentModel
from ..dao.TournamentDAO import TournamentDAO
from ..controllers.PlayerController import PlayerController
from ..models.PlayerModel import PlayerModel


class MissingPlayerException(Exception):
    pass


class PlayerCountException(Exception):
    pass


class TournamentController:

    def __init__(self):
        self.player_controller = PlayerController()
        self.tournament_dao = TournamentDAO()
        self.model = TournamentModel()

    def create_tournament(self, players_ids: List[int]):
        players = []
        for player_id in players_ids:
            player = self.player_dao.get_player(player_id)
            if player is None:
                raise MissingPlayerException(f"Player not found")
            players.append(player)

        creation_date = datetime.now()
        # Vérif len(players) == 8
        #
        # erreur : joueurs manquants PlayerCountError
        # creation_date_str =
        tournament = TournamentModel(players, creation_date)
        self.tournament_dao.create_tournament(tournament)

    def get_tournaments(self):
        raise NotImplementedError

    def get_tournament(self, tournament_id):
        raise NotImplementedError

    def update_tournament(self, tournament_id, updated_tournament):
        raise NotImplementedError

    def delete_tournament(self, tournament_id):
        raise NotImplementedError
