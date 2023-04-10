from backend.games.GameModel import GameStatus


class GameService:
    def __init__(self, game_dao, round_service):
        self.game_dao = game_dao
        self.round_service = round_service

    def set_players_score(self, game, p1_score, p2_score):
        game.set_players_score(p1_score, p2_score)
        self.round_service.update_round_status(game.round_id)
