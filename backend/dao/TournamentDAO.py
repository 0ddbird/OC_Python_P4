import os
from tinydb import TinyDB, Query
from backend.models.TournamentModel import TournamentModel
from ..serializers.TournamentSerializer import TournamentSerializer


class TournamentDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "tournaments.json"))
        self.serializer = TournamentSerializer()

    def create_tournament(self, tournament: TournamentModel):
        serialized_tournament = self.serializer.serialize(tournament)
        try:
            return self.db.insert(serialized_tournament)
        except Exception as e:
            print(e)

    def get_tournaments(self):
        tournament_records = self.db.all()
        tournaments = []
        for tournament_record in tournament_records:
            tournament_record["tournament_id"] = tournament_record.doc_id
            tournament = self.serializer.deserialize(tournament_record)
            tournaments.append(tournament)
        return tournaments

    def get_tournament(self, tournament_id):
        try:
            tournament_record = self.db.get(doc_id=tournament_id)
            if not tournament_record:
                raise Exception(
                    f"Tournament with id {tournament_id} not found"
                )
            tournament_record["tournament_id"] = tournament_id
            tournament = self.serializer.deserialize(tournament_record)
            return tournament
        except Exception as e:
            print(e)

    def update_tournament(self, tournament_id, updated_tournament):
        tournament = Query()
        self.db.update(
            updated_tournament, tournament.t_id.matches(tournament_id)
        )

    def delete_tournament(self, tournament_id):
        tournament = Query()
        self.db.remove(tournament.t_id.matches(tournament_id))
