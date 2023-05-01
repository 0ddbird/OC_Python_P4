from random import shuffle
from typing import Iterable, List

from backend.abstract.typing.model_typing import ForeignKey


def shuffle_and_pair_players(
    numbers: Iterable[int],
) -> tuple[tuple[int, int], ...]:
    numbers_copy = list(numbers)
    shuffle(numbers_copy)

    pairs = tuple(
        (numbers_copy[i], numbers_copy[i + 1])
        for i in range(0, len(numbers_copy), 2)
    )
    return pairs


def get_opponents_history(tournament_snapshot):
    opponents_history = {}

    for game_results in tournament_snapshot:
        player_ids = list(game_results.keys())
        p1_id, p2_id = player_ids[0], player_ids[1]

        if p1_id not in opponents_history:
            opponents_history[p1_id] = []
        opponents_history[p1_id].append(p2_id)

        if p2_id not in opponents_history:
            opponents_history[p2_id] = []
        opponents_history[p2_id].append(p1_id)

    return opponents_history


def rank_players(tournament_snapshot: list[dict]):
    player_scores = {}
    for game_results in tournament_snapshot:
        for player_id, score in game_results.items():
            if player_id not in player_scores:
                player_scores[player_id] = 0
            player_scores[player_id] += score.value
    sorted_player_scores = sorted(
        player_scores.items(), key=lambda x: x[1], reverse=True
    )
    return sorted_player_scores


def sort_and_pair_players(
    remaining_players, history
) -> list[tuple[ForeignKey]]:
    pairings = []

    return pairings
