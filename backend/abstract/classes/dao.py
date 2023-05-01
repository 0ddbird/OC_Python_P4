from abc import ABC


class DAO(ABC):
    @staticmethod
    def pop_id(obj: dict):
        try:
            del obj["id"]
        except KeyError:
            pass
