import os
from tinydb import TinyDB

from backend.abstract.classes.dao import DAO
from backend.abstract.exceptions.dao_exceptions import (
    TournamentNotFoundException,
)
from backend.abstract.typing.model_typing import PrimaryKey
from backend.tournaments.models.model import TournamentModel
from backend.tournaments.serializer import TournamentSerializer


class TournamentDAO(DAO):
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("tournaments")
        self.serializer = TournamentSerializer()

    def create(self, tournament: TournamentModel) -> PrimaryKey:
        serialized_tournament = self.serializer.serialize(tournament)
        self.pop_id(serialized_tournament)
        return self.table.insert(serialized_tournament)

    def get(self, id: PrimaryKey) -> TournamentModel:
        record = self.table.get(doc_id=id)
        if record is None:
            raise TournamentNotFoundException(id)
        record["id"] = record.doc_id
        return self.serializer.deserialize(record)

    def get_all(self) -> list[TournamentModel]:
        tournament_records = self.table.all()
        tournaments = []
        for tournament_record in tournament_records:
            tournament_record["id"] = tournament_record.doc_id
            tournament = self.serializer.deserialize(tournament_record)
            tournaments.append(tournament)
        return tournaments

    def update(self, id: PrimaryKey, tournament: TournamentModel):
        serialized_tournament = self.serializer.serialize(tournament)
        self.pop_id(serialized_tournament)
        self.table.update(serialized_tournament, doc_ids=[id])

    def delete(self, tournament_id: PrimaryKey) -> None:
        self.table.remove(doc_ids=[tournament_id])
