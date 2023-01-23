from dao.PlayerDAO import PlayerDAO
from models.PlayerModel import PlayerModel


class PlayerController:
    def __init__(self):
        self.dao = PlayerDAO()

    def create_player(self, p_id, first_name, last_name, birthdate, elo):
        player = PlayerModel(p_id, first_name, last_name, birthdate, elo)
        self.dao.create_player(player)

    def get_players(self):
        return self.dao.get_players()

    def get_player(self, player_id):
        return self.dao.get_player(player_id)

    def update_player(self, player: PlayerModel):
        self.dao.update_player(player)

    def delete_player(self, player_id):
        self.dao.delete_player(player_id)
