class TournamentValidationException(Exception):
    pass


def validate_tournament_fields(name, rounds, location, description, players_ids):
    errors = []

    if name is None or name == "":
        errors.append("Name is required")

    if rounds is None or rounds < 1:
        errors.append("Rounds must be greater than 0")

    if location is None or location == "":
        errors.append("Location is required")

    if description is None:
        errors.append("Description is required")

    if players_ids is None or len(players_ids) < 2:
        errors.append("A tournament must have at least 2 players")

    if errors:
        raise TournamentValidationException(errors)

    return None
