from random import shuffle
from typing import List, Tuple

from ..dao.GameDAO import GameDAO
from ..dao.PlayerDAO import PlayerDAO
from ..dao.TournamentDAO import TournamentDAO
from ..dao.RoundDAO import RoundDAO
from ..models.GameModel import GameModel
from ..models.RoundModel import RoundModel
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
        self.game_dao = GameDAO()

    def create_tournament(
        self,
        name: str,
        location: str,
        description: str,
        players_ids: Tuple[int],
        max_rounds: int,
    ):
        for player_id in players_ids:
            player = self.player_dao.get_player(player_id)
            if player is None:
                raise MissingPlayerException(f"Player with ID {player_id} not found")

        tournament = TournamentModel(
            name=name,
            location=location,
            description=description,
            players_ids=players_ids,
            max_rounds=max_rounds,
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
        print(tournament)
        return self.serializer.serialize(tournament)

    @staticmethod
    def shuffle_players(players_ids: List[int]):
        players_ids_copy = players_ids.copy()
        shuffle(players_ids_copy)
        return players_ids_copy

    def create_game(self, p1_id, p2_id):
        game = GameModel(p1_id, p2_id)
        return self.game_dao.create_game(game)

    def create_first_round(self, tournament):
        """

        1. Shuffle all the players IDs
        2. Pair the players and store them as an instance of GameModel
        3. Create an instance of Round model with all the games
        4. Update the games with the round ID.
        6. Update the tournament status from "not started" to
        "round_in_progress"
        7. Update the tournament "current_round" to current_round + 1
        5. Return the round ID.

        """

        tournament_id = tournament.t_id
        players_ids = tournament.players_ids
        shuffled_p_ids = self.shuffle_players(players_ids)

        games_ids = []

        for i in range(0, len(shuffled_p_ids), 2):
            p1_id = shuffled_p_ids[i]
            p2_id = shuffled_p_ids[i + 1]
            game_id = self.create_game(p1_id, p2_id)
            games_ids.append(game_id)

        round = RoundModel(games_ids, tournament_id, 1)
        round_id = self.round_dao.create_round(round)
        print(f"TournamentController: {round_id=}")
        games = self.game_dao.get_games_by_ids(games_ids)
        print(f"TournamentController: {games=}")
        for game in games:
            game.set_round_id(round_id)
            self.game_dao.update_game(game)

        return round_id

    def create_next_round(self, tournament_id):
        """

        This method creates a new Round for a tournament with tournament_id.
        1. Find tournament
        2. Check the status of the tournament:
            If tournament ended : return error
            If a round is in progress: return error
            If current round == 0 : call self.create_first_round.
            If current round > 0 <= tournament.max_round : call
            self.create_next_round
        """
        tournament = self.tournament_dao.get_tournament(tournament_id)
        print(f"TournamentController: {tournament=}")
        return self.create_first_round(tournament)

    def update_tournament(self, tournament_id, updated_tournament):
        raise NotImplementedError

    def delete_tournament(self, tournament_id):
        raise NotImplementedError
