class PlayerNotFoundException(Exception):
    def __init__(self, id) -> None:
        self.message = f"Player with id {id} not found"
        super().__init__(self.message)


class PlayerCreationException(Exception):
    def __init__(self) -> None:
        self.message = "Couldn't create player"
        super().__init__(self.message)


class RoundNotFoundException(Exception):
    def __init__(self, id) -> None:
        self.message = f"Round with id {id} not found"
        super().__init__(self.message)


class TournamentNotFoundException(Exception):
    def __init__(self, id) -> None:
        self.message = f"Tournament with id: {id} not found"
        super().__init__(self.message)
