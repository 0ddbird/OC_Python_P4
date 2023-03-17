class TournamentModel:
    def __init__(self):
        self.t_id = None
        self.name = None
        self.location = None
        self.start_date = None
        self.end_date = None
        self.max_rounds = None
        self.curr_round = None
        self.players = None
        self.description = None

    def __str__(self):
        return (
            f"{self.name} {self.location} {self.start_date}"
            f" {self.end_date} {self.max_rounds} {self.curr_round} "
            f"{self.players} {self.description}"
        )

    def __repr__(self):
        return (
            f"{self.name} {self.location} {self.start_date}"
            f" {self.end_date} {self.max_rounds} {self.curr_round} "
            f"{self.players} {self.description}"
        )