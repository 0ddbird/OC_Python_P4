from dataclasses import dataclass
from datetime import date, datetime
from enum import Enum
from typing import Optional

from backend.dao.GameDAO import GameDAO
from backend.dao.RoundDAO import RoundDAO
from backend.models.GameModel import GameModel
from backend.models.model_typing import ForeignKey, PrimaryKey
from backend.models.RoundModel import RoundModel
from backend.utils import shuffle_players, sort_by_score


class TournamentStatus(Enum):
    TO_START = (0,)
    STARTED = (1,)
    ROUND_OPEN = (2,)
    ENDED = (3,)


@dataclass
class TournamentModel:
    name: str
    location: str
    description: str
    players_ids: tuple[ForeignKey, ...]
    max_rounds: int
    rounds_ids: tuple[ForeignKey, ...] = ()
    current_round: int = 0
    status: TournamentStatus = TournamentStatus.TO_START
    start_datetime: date = datetime.now()
    end_datetime: Optional[date] = None
    id: Optional[PrimaryKey] = None
    game_dao = GameDAO()
    round_dao = RoundDAO()

    def set_to_next_round(self) -> None:
        if self.current_round == self.max_rounds:
            raise ValueError("All the rounds are finished.")
        self.current_round += 1

    def set_end_date(self) -> None:
        if self.end_datetime is not None:
            raise ValueError("End date is already defined")
        self.end_datetime = datetime.now()

    def create_game(self, p1_id, p2_id) -> PrimaryKey:
        game = GameModel(
            p1_id=p1_id,
            p2_id=p2_id,
        )
        return self.game_dao.create_game(game)

    def create_multiple_games(
        self,
        p_ids: tuple[PrimaryKey],
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
    ) -> PrimaryKey:
        round = RoundModel(
            games_ids=games_ids,
            tournament_id=self.id,
            round_number=self.current_round + 1,
        )
        return self.round_dao.create_round(round)

    def update_games(
        self,
        games_ids: tuple[PrimaryKey],
        round_id: PrimaryKey,
    ) -> None:
        games = self.game_dao.get_games_by_id(games_ids)

        for game in games:
            game.set_round_id(round_id)
            self.game_dao.update_game(game)

    def create_next_round(self) -> ForeignKey:
        players_ids = list(self.players_ids)
        players_pairs = []

        # CASE 1: first round
        if self.status == TournamentStatus.TO_START:
            players_pairs = shuffle_players(players_ids)

        # CASE 2: next rounds
        if self.status == TournamentStatus.STARTED:
            players_pairs = sort_by_score(players_ids)

        # Create games based on players pairs
        games_ids = self.create_multiple_games(players_pairs)

        # Create round based on the games IDs
        round_id = self.create_round(games_ids)

        # Insert the Round ID into each Game record
        self.update_games(games_ids, round_id)

        # Append Tournament.rounds_ids
        current_rounds_ids = list(self.rounds_ids)

        current_rounds_ids.append(round_id)
        self.rounds_ids = tuple(current_rounds_ids)

        # Set Tournament status to ROUND_OPEN
        self.status = TournamentStatus.ROUND_OPEN

        return round_id
