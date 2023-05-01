game_1 = {
    "p1_id": 1,
    "p1_score": 1.0,
    "p2_id": 2,
    "p2_score": 0.0,
}

game_2 = {
    "p1_id": 3,
    "p1_score": 1.0,
    "p2_id": 4,
    "p2_score": 0.0,
}

game_3 = {
    "p1_id": 5,
    "p1_score": 0.5,
    "p2_id": 6,
    "p2_score": 0.5,
}

games = [game_1, game_2, game_3]


def get_player_history(games):
    history = {}
    for game in games:
        p1_id = game.get("p1_id")
        p2_id = game.get("p2_id")
        if not history.get("p1_id"):
            history[p1_id] = game.get("p2_id")
            history[p2_id] = game.get("p1_id")
    return history


history = get_player_history(games)
print(history)


def rank_players(games):
    ranking = []
    for game in games:
        pass
