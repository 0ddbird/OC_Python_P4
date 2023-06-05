import datetime
import re


def validate_chess_id(chess_id):
    pattern = re.compile(r"[A-Z]{2}\d{5}")
    return bool(pattern.fullmatch(chess_id))


def validate_birthdate(birthdate):
    try:
        birthdate = datetime.datetime.strptime(birthdate, "%Y-%m-%d")
        return (datetime.datetime.now() - birthdate) > datetime.timedelta(
            days=365
        )
    except ValueError:
        return False


def validate_elo(elo):
    try:
        elo = int(elo)
        return elo >= 0
    except ValueError:
        return False


def validate_player_fields(chess_id: str, birthdate: str, elo: str) -> None:
    if not validate_chess_id(chess_id):
        raise ValueError("Invalid chess ID")

    if not validate_birthdate(birthdate):
        raise ValueError("Invalid birthdate")

    if not validate_elo(elo):
        raise ValueError
