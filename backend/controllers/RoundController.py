from flask import Request
from backend.dao.RoundDAO import RoundDAO
from backend.dao.TournamentDAO import TournamentDAO
from backend.models.model_typing import PrimaryKey, SerializedRound
from backend.serializers.RoundSerializer import RoundSerializer


class RoundController:
    def __init__(self) -> None:
        self.dao: RoundDAO = RoundDAO()
        self.tournamentDAO: TournamentDAO = TournamentDAO()
        self.serializer: RoundSerializer = RoundSerializer()

    def get_round(self, id: PrimaryKey) -> SerializedRound:
        round = self.dao.get_round(id)
        return self.serializer.serialize(round)

    def update_round(self, id: PrimaryKey, http_request: Request) -> None:
        round = self.get_round(id)
        self.dao.update_round(round)
