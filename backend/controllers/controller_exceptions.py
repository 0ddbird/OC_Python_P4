class PlayerCountException(Exception):
    def __init__(self):
        self.message = "Not enough players"
        super().__init__(self.message)


class TournamentEndedException(Exception):
    def __init__(self):
        self.message = "This tournament has ended"
        super().__init__(self.message)


class RoundOpenException(Exception):
    def __init__(self):
        self.message = "A round is already open"
        super().__init__(self.message)
