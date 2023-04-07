import os
from tinydb import TinyDB

from backend.abstract.exceptions.dao_exceptions import (
    TournamentNotFoundException,
)
from backend.abstract.typing.model_typing import PrimaryKey
from backend.tournaments.TournamentModel import TournamentModel
from backend.tournaments.TournamentSerializer import TournamentSerializer


class TournamentDAO:
    def __init__(self) -> None:
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("tournaments")
        self.serializer = TournamentSerializer()

    def create_tournament(self, tournament: TournamentModel) -> PrimaryKey:
        serialized_tournament = self.serializer.serialize(tournament)
        try:
            del serialized_tournament["id"]
        except KeyError:
            pass
        return self.table.insert(serialized_tournament)

    def get_tournaments(self):
        tournament_records = self.table.all()
        tournaments = []
        for tournament_record in tournament_records:
            tournament_record["id"] = tournament_record.doc_id
            tournament = self.serializer.deserialize(tournament_record)
            tournaments.append(tournament)
        return tournaments

    def get_tournament(self, id: PrimaryKey) -> TournamentModel:
        record = self.table.get(doc_id=id)
        if record is None:
            raise TournamentNotFoundException(id)
        record["id"] = record.doc_id
        return self.serializer.deserialize(record)

    def update_tournament(
        self,
        tournament_id: PrimaryKey,
        updated_tournament: TournamentModel,
    ):
        serialized_tournament = self.serializer.serialize(updated_tournament)
        try:
            del serialized_tournament["id"]
        except KeyError:
            pass
        self.table.update(serialized_tournament, doc_ids=[tournament_id])

    def delete_tournament(self, tournament_id: PrimaryKey) -> None:
        raise NotImplementedError
