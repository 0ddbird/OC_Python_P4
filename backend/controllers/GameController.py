from backend.models.GameModel import (
    GameModel,
)


class GameController:
    def __init__(
        self,
    ):
        self.game = GameModel()

    # def create_game(self):
    #     self.game.create_game()
    #
    # def get_game(self, game_id):
    #     return self.game.get_game(game_id)
    #
    # def update_game(self, game_id, updated_game):
    #     self.game.update_game(game_id, updated_game)
    #
    # def delete_game(self, game_id):
    #     self.game.delete_game(game_id)
    #
    # def get_all_games(self):
    #     return self.game.get_all_games()
