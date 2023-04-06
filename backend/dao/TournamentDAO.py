import os
from tinydb import TinyDB, Query

from ..models.model_typing import PrimaryKey
from ..models.TournamentModel import TournamentModel
from ..serializers.TournamentSerializer import TournamentSerializer


class TournamentNotFoundException(Exception):
    def __init__(self, t_id):
        self.message = f"Can't find the tournament with id: {t_id}"
        super().__init__(self.message)


class TournamentDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        self.table = self.db.table("tournaments")
        self.serializer = TournamentSerializer()

    def create_tournament(self, tournament: TournamentModel):
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
            print(tournament)
            tournaments.append(tournament)
        return tournaments

    def get_tournament(self, id: PrimaryKey) -> TournamentModel:
        record = self.table.get(doc_id=id)
        if record is None:
            raise TournamentNotFoundException(id)
        record["id"] = record.doc_id
        return self.serializer.deserialize(record)

    def update_tournament(self, tournament_id, updated_tournament):
        tournament = Query()
        serialized_tournament = self.serializer.serialize(updated_tournament)
        del serialized_tournament["id"]
        self.table.update(
            updated_tournament, tournament.t_id.matches(tournament_id)
        )

    def delete_tournament(self, tournament_id):
        tournament = Query()
        self.table.remove(tournament.t_id.matches(tournament_id))
