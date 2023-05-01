from random import shuffle
from typing import Iterable


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


def sort_and_pair_players(
    player_scores, history
) -> tuple[tuple[int, int], ...]:
    ranking = sorted(player_scores, key=lambda x: x[0], reverse=True)

    pairs = []

    while len(ranking) > 1:
        score, player_id = ranking[0]
        next_score = ranking[1][0]
        next_player_id = ranking[1][1]

        potential_next_opponents = [
            id
            for score, id in ranking
            if score == next_score and id != player_id
        ]
        if len(potential_next_opponents) == 1 or all(
            opponent in history[player_id]
            for opponent in potential_next_opponents
        ):
            pairs.append((player_id, next_player_id))
            ranking = [
                pair
                for pair in ranking
                if pair[1] not in (player_id, next_player_id)
            ]
        else:
            for opponent_id in potential_next_opponents:
                if opponent_id not in history[player_id]:
                    pairs.append((player_id, opponent_id))
                    ranking = [
                        pair
                        for pair in ranking
                        if pair[1] not in (player_id, opponent_id)
                    ]
                    break

    return tuple(pairs)
