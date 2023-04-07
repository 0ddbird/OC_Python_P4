import os

from tinydb import TinyDB
import gc

DB = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))


def reset_db() -> None:
    tables = ["players", "tournaments", "games", "rounds"]
    for table in tables:
        table = DB.table(table)
        table.truncate()
        gc.collect()
        DB.close()
