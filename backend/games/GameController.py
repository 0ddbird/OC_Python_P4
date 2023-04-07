from backend.games.GameSerializer import GameSerializer


class GameController:
    def __init__(self):
        self.serializer = GameSerializer()
