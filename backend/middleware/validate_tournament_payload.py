class TournamentValidationException(Exception):
    pass


def validate_tournament_fields(
    name,
    location,
    description,
    players_ids,
    max_rounds,
):
    errors = []

    if name is None or name == "":
        errors.append("Name is required")

    try:
        int_max_rounds = int(max_rounds)
        if int_max_rounds < 1:
            errors.append("Rounds must be greater than 0")
    except ValueError:
        errors.append("Max rounds must be a number")
    except TypeError:
        errors.append("Max rounds is required")

    if location is None or location == "":
        errors.append("Location is required")

    if description is None or description == "":
        errors.append("Description is required")

    if players_ids is None or len(players_ids) < 2:
        errors.append("A tournament must have at least 2 players")

    return {"is_valid": len(errors) == 0, "errors": errors}
