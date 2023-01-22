from dataclasses import asdict
from tinydb import TinyDB, Query
from models.PlayerModel import PlayerModel


class PlayerDAO:
    db = TinyDB("./db/players.json")

    def create_player(self, player: PlayerModel):
        player_dict = asdict(player)
        self.db.insert(player_dict)

    def get_players(self):
        return self.db.all()

    def get_player(self, player_id):
        return self.db.search(Query().p_id.matches(player_id))

    def update_player(self, player_id, updated_player):
        user = Query()
        self.db.update(updated_player, user.p_id.matches(player_id))

    def delete_player(self, player_id):
        user = Query()
        self.db.remove(user.p_id.matches(player_id))
