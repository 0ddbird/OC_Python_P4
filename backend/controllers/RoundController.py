from backend.models.RoundModel import RoundModel


class RoundController:
    def __init__(self):
        self.round = RoundModel()

    def create_round(self):
        self.round.create_round()

    def get_round(self, round_id):
        return self.round.get_round(round_id)

    def update_round(self, round_id, updated_round):
        self.round.update_round(round_id, updated_round)

    def delete_round(self, round_id):
        self.round.delete_round(round_id)
