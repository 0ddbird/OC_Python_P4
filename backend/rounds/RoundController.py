from flask import Request
from backend.rounds.RoundDAO import RoundDAO
from backend.tournaments.TournamentDAO import TournamentDAO
from backend.abstract.typing.model_typing import PrimaryKey, SerializedRound
from backend.rounds.RoundSerializer import RoundSerializer


class RoundController:
    def __init__(self) -> None:
        self.dao: RoundDAO = RoundDAO()
        self.tournamentDAO: TournamentDAO = TournamentDAO()
        self.serializer: RoundSerializer = RoundSerializer()

    def get_round(self, id: PrimaryKey) -> SerializedRound:
        round = self.dao.get_round(id)
        return self.serializer.serialize(round)

    def get_all_rounds(self) -> list[SerializedRound]:
        rounds = self.dao.get_all_rounds()
        return [self.serializer.serialize(round) for round in rounds]

    def update_round(self, id: PrimaryKey, http_request: Request) -> None:
        round = self.get_round(id)
        self.dao.update_round(round)
