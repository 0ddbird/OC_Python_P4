import os
from tinydb import TinyDB, Query


from ..models.TournamentModel import TournamentModel
from ..serializers.TournamentSerializer import TournamentSerializer


class TournamentNotFoundException(Exception):
    def __init__(self, t_id):
        self.message = f"Can't find the tournament with id: {t_id}"
        super().__init__(self.message)


class TournamentDAO:
    def __init__(self):
        self.db = TinyDB(os.path.join(os.getcwd(), "db", "tournaments.json"))
        self.serializer = TournamentSerializer()

    def create_tournament(self, tournament: TournamentModel):
        serialized_tournament = self.serializer.serialize(tournament)
        tournament_record_id = self.db.insert(serialized_tournament)
        return tournament_record_id

    def get_tournaments(self):
        tournament_records = self.db.all()
        tournaments = []
        for tournament_record in tournament_records:
            tournament_record["tournament_id"] = tournament_record.doc_id
            tournament = self.serializer.deserialize(tournament_record)
            tournaments.append(tournament)
        return tournaments

    def get_tournament(self, tournament_id):
        tournament_record = self.db.get(doc_id=tournament_id)
        if tournament_record is None:
            raise TournamentNotFoundException(tournament_id)
        tournament_record["tournament_id"] = tournament_id
        return self.serializer.deserialize(tournament_record)

    def update_tournament(self, tournament_id, updated_tournament):
        tournament = Query()
        self.db.update(updated_tournament, tournament.t_id.matches(tournament_id))

    def delete_tournament(self, tournament_id):
        tournament = Query()
        self.db.remove(tournament.t_id.matches(tournament_id))
