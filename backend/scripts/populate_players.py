import datetime
import random
import string

from backend.players.PlayerDAO import PlayerDAO
from backend.players.PlayerModel import PlayerModel

used_ids = set()


def gen_id():
    while True:
        p_id = "".join(random.choice(string.ascii_uppercase) for _ in range(2))
        p_id += "".join(random.choice(string.digits) for _ in range(5))
        if p_id not in used_ids:
            used_ids.add(p_id)
            yield p_id


generator = gen_id()
player_dao = PlayerDAO()

for i in range(1, 11):
    p_id = next(generator)
    first_name = "FirstName_" + str(i)
    last_name = "LastName_" + str(i)
    year = random.randint(1970, 2000)
    month = random.randint(1, 12)
    day = random.randint(1, 28)
    birthdate = datetime.datetime(year, month, day)
    elo = random.randint(1000, 3000)
    player = PlayerModel(p_id, first_name, last_name, birthdate, elo)
    player_dao.create_player(player)
