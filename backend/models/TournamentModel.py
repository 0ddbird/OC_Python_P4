class TournamentModel:
    def __init__(
        self, name, max_rounds, location, description, players_ids,
            creation_date,
            current_round, status, t_id=None,

    ):
        self.t_id = t_id
        self.name = name
        self.max_rounds = max_rounds
        self.location = location
        self.description = description
        self.players_ids = players_ids
        self.creation_date = creation_date
        self.current_round = current_round
        self.end_date = None
        self.status = status

    def __repr__(self):
        return f"TournamentModel(t_id={self.t_id}, name={self.name}, max_rounds={self.max_rounds}, location={self.location}, description={self.description}, players_ids={self.players_ids}, creation_date={self.creation_date}, current_round={self.current_round}, end_date={self.end_date}, tournament_status={self.status})"
