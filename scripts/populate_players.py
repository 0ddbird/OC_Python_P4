from dataclasses import asdict
from models.PlayerModel import PlayerModel
from tinydb import TinyDB
import random
import string


used_ids = set()


def gen_id():
    while True:
        p_id = "".join(random.choice(string.ascii_uppercase) for _ in range(2))
        p_id += "".join(random.choice(string.digits) for _ in range(5))
        if p_id not in used_ids:
            used_ids.add(p_id)
            yield p_id


db = TinyDB("../db/players.json")
generator = gen_id()

for i in range(1, 11):
    p_id = next(generator)
    first_name = "FirstName" + str(i)
    last_name = "LastName" + str(i)
    birthdate = (
        random.randint(1970, 2000),
        random.randint(1, 12),
        random.randint(1, 28),
    )
    elo_score = random.randint(1000, 3000)

    player = PlayerModel(p_id, first_name, last_name, birthdate, elo_score)
    player_dict = asdict(player)
    db.insert(player_dict)
