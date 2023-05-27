from abc import ABC
from contextlib import contextmanager
from tinydb import TinyDB
import os


class DAO(ABC):
    def __init__(self, serializer, table_name: str):
        self.serializer = serializer
        self.table_name = table_name

    @staticmethod
    def pop_id(obj: dict):
        try:
            del obj["id"]
        except KeyError:
            pass

    @contextmanager
    def open_db(self):
        db = TinyDB(os.path.join(os.getcwd(), "db", "db.json"))
        table = db.table(self.table_name)
        try:
            yield table
        finally:
            db.close()

    def create(self, model):
        serialized_model = self.serializer.serialize(model)
        self.pop_id(serialized_model)
        with self.open_db() as table:
            return table.insert(serialized_model)

    def get(self, id):
        with self.open_db() as table:
            record = table.get(doc_id=id)
            if not record:
                raise Exception(f"{self.table_name.capitalize()} {id} not found")
            record["id"] = record.doc_id
            return self.serializer.deserialize(record)

    def get_all(self):
        with self.open_db() as table:
            records = table.all()
            for record in records:
                record["id"] = record.doc_id
            return [self.serializer.deserialize(record) for record in records]

    def get_multiple(self, ids):
        return [self.get(id) for id in ids]

    def update(self, model):
        serialized_model = self.serializer.serialize(model)
        self.pop_id(serialized_model)
        with self.open_db() as table:
            table.update(serialized_model, doc_ids=[model.id])

    def delete(self, id):
        with self.open_db() as table:
            table.remove(doc_ids=[id])
