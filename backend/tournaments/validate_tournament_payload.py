from typing import Iterable

from backend.abstract.typing.model_typing import ForeignKey


class TournamentValidationException(Exception):
    pass


def validate_tournament_fields(
    name: str,
    location: str,
    description: str,
    players_ids: Iterable[ForeignKey],
    max_rounds: int,
) -> None:
    if name is None or name == "":
        raise ValueError
    try:
        int_max_rounds = int(max_rounds)
        if int_max_rounds < 1:
            raise ValueError
    except ValueError:
        raise
    except TypeError:
        raise

    if location is None or location == "":
        raise ValueError

    if description is None or description == "":
        raise ValueError

    if players_ids is None or len(players_ids) < 2:
        raise ValueError
