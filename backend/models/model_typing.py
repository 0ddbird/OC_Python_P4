import re
from typing import Pattern

ForeignKey = int
PrimaryKey = int
ChessID: Pattern = re.compile(r"^[A-Z]{2}\d{5}$")
