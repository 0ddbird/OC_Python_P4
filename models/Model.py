from tinydb import TinyDB, Query


class Model:
    def __init__(self):
        self.db = TinyDB("../db.json")
