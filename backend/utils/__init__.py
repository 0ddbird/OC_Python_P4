from random import shuffle


def shuffle_players(numbers: list[int]) -> list[int]:
    numbers_copy = numbers.copy()
    shuffle(numbers_copy)
    return numbers_copy


def sort_by_score(numbers: list[int]) -> list[int]:
    raise NotImplementedError
