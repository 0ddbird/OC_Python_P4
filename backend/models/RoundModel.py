from dataclasses import asdict


class RoundModel:
    def __init__(self):
        self.r_id = None
        self.r_num = None
        self.r_players = None

    def to_dict(self):
        return asdict(self)

    def __str__(self):
        return f"{self.r_players}"

    def __repr__(self):
        return f"{self.r_players}"

    # def create_round(self):
    #     self.dao.create_round(self)
    #
    # def get_rounds(self):
    #     return self.dao.get_rounds()
    #
    # def get_round(self, round_id):
    #     return self.dao.get_round(round_id)
    #
    # def update_round(self, round_id, updated_round):
    #     self.dao.update_round(round_id, updated_round)
    #
    # def delete_round(self, round_id):
    #     self.dao.delete_round(round_id)

    def get_round_players(self):
        return self.r_players
