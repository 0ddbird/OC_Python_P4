from backend.controllers.PlayerController import PlayerController
from backend.exceptions.dao import PlayerCreationException
from backend.router.utils import api_response

controller = PlayerController()


def handle_get_players():
    players = controller.get_all_players()
    return api_response("OK", 200, players)


def handle_post_player(http_request):
    player = {
        "chess_id": http_request.json.get("chess_id"),
        "first_name": http_request.json.get("first_name"),
        "last_name": http_request.json.get("last_name"),
        "birthdate": http_request.json.get("birthdate"),
        "elo": http_request.json.get("elo"),
    }
    try:
        player_id = controller.create_player(player)
        return api_response("OK", 201, {"id": player_id})
    except PlayerCreationException as e:
        return api_response("Error", 400, f"Error in PlayerController: {e}")


def handle_get_player(player_id):
    player = controller.get_player(player_id)
    return api_response("OK", 200, player)


def handle_update_player(player_id, http_request):
    player_data = {
        "player_id": player_id,
        "chess_id": http_request.json.get("chess_id"),
        "first_name": http_request.json.get("first_name"),
        "last_name": http_request.json.get("last_name"),
        "birthdate": http_request.json.get("birthdate"),
        "elo": http_request.json.get("elo"),
    }

    try:
        updated_player_id = controller.update_player(player_data)
        return api_response("OK", 200, {"id": updated_player_id})

    except Exception as e:
        return api_response("Error", 400, f"Error in PlayerController: {e}")


def handle_delete_player(player_id):
    try:
        controller.delete_player(int(player_id))
        return api_response("OK", 204, {"id": player_id})
    except Exception as e:
        return api_response("Error", 400, f"Error in PlayerController: {e}")
