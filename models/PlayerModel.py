import datetime
from dataclasses import dataclass, asdict


@dataclass
class PlayerModel:
    p_id: str
    first_name: str
    last_name: str
    birthdate: datetime.datetime
    elo: int

    def to_dict(self):
        data = asdict(self)
        data["birthdate"] = self.birthdate.isoformat()
        return data
