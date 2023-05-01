import re
from typing import Pattern

Key = int
ForeignKey = Key
PrimaryKey = Key

ChessID: Pattern = re.compile(r"^[A-Z]{2}\d{5}$")

SerializedModel = dict
SerializedTournament = SerializedModel
SerializedPlayer = SerializedModel
SerializedRound = SerializedModel
SerializedGame = SerializedModel

Score = float
