from flask import make_response

from backend.controllers.TournamentController import TournamentController
from backend.middleware.validate_tournament_payload import (
    validate_tournament_fields,
)
from backend.router.response_codes import ResCode


class TournamentRouter:
    def __init__(self):
        self.controller = TournamentController()

    def handle_get_tournament(self, tournament_id):
        try:
            tournament = self.controller.get_tournament(tournament_id)
            return make_response(
                {
                    "message": "Tournament found",
                    "payload": tournament,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find tournament",
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_tournaments(self):
        try:
            tournaments = self.controller.get_all_tournaments()
            return make_response(
                {
                    "message": "Tournaments fetched successfully",
                    "payload": tournaments,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't find tournament",
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_post_tournament(self, request):
        name = request.json.get("name")
        max_rounds = request.json.get("max_rounds")
        location = request.json.get("location")
        description = request.json.get("description")
        player_ids = tuple(request.json.get("players_ids"))

        tournament_data = validate_tournament_fields(
            name,
            location,
            description,
            player_ids,
            max_rounds,
        )
        if not tournament_data["is_valid"]:
            return make_response(
                {
                    "message": "Please provide valid values",
                    "error": tournament_data["errors"],
                },
                ResCode.BAD_REQUEST.value,
            )

        try:
            tournament = self.controller.create_tournament(
                name,
                location,
                description,
                player_ids,
                max_rounds,
            )
            return make_response(
                {
                    "message": "Tournament created successfully",
                    "payload": tournament,
                },
                ResCode.CREATED.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't create tournament",
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_next_round(self, tournament_id):
        try:
            tournament = self.controller.get_tournament(tournament_id)
            if tournament.status == "awaiting round results":
                return make_response(
                    {
                        "message": "Please wait for the current round to finish",
                    },
                    ResCode.BAD_REQUEST.value,
                )
            round_id = self.controller.create_next_round(tournament_id)
            return make_response(
                {
                    "message": "Tournament started successfully",
                    "payload": round_id,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            print(e)
            return make_response(
                {
                    "message": "Can't find tournament",
                },
                ResCode.BAD_REQUEST.value,
            )
