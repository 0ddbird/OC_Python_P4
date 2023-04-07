from flask import make_response, Response, Request, redirect, url_for

from backend.abstract.classes.Router import Router
from backend.tournaments.TournamentController import TournamentController
from backend.middleware.validate_tournament_payload import (
    validate_tournament_fields,
)
from backend.abstract.typing.model_typing import PrimaryKey
from backend.abstract.response_codes import ResCode


class TournamentRouter(Router):
    def __init__(self) -> None:
        self.controller = TournamentController()

    def handle_get_tournament(self, tournament_id) -> Response:
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
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_tournaments(self) -> Response:
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
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_post_tournament(self, request: Request) -> Response:
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
                {"message": "Can't create tournament", "error": e},
                ResCode.BAD_REQUEST.value,
            )

    def handle_delete_tournament(self, tournament_id: PrimaryKey) -> Response:
        try:
            self.controller.delete_tournament(tournament_id)
            return make_response(
                {
                    "message": "Tournament deleted successfully",
                },
                ResCode.NO_CONTENT.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Can't delete tournament",
                    "error": e,
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_create_next_round(self, tournament_id: PrimaryKey) -> Response:
        try:
            round = self.controller.create_next_round(
                tournament_id=tournament_id
            )
            return make_response(
                {
                    "message": "Round created",
                    "payload": round,
                },
                ResCode.CREATED.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Error while creating new round",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_tournament_rounds(self, t_id: PrimaryKey) -> Response:
        try:
            rounds = self.controller.get_tournament_rounds(tournament_id=t_id)
            return make_response(
                {
                    "message": "Tournament rounds found",
                    "payload": rounds,
                },
                ResCode.OK.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Error while fetching rounds",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_get_tournament_round(
        self,
        tournament_id: PrimaryKey,
        round_number: int,
    ) -> Response:
        try:
            round_id = self.controller.get_round_id(
                tournament_id=tournament_id, round_number=round_number
            )
            return redirect(url_for("rounds.round", round_id=round_id))
        except Exception as e:
            return make_response(
                {
                    "message": "Error while fetching round",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )

    def handle_update_games(
        self,
        tournament_id: PrimaryKey,
        round_number: int,
        request: Request,
    ) -> Response:
        try:
            payload = request.json
            self.controller.update_games(tournament_id, round_number, payload)
            return make_response(
                {
                    "message": f"Tournament round #{round_number} updated",
                    "payload": round,
                },
                ResCode.NO_CONTENT.value,
            )
        except Exception as e:
            return make_response(
                {
                    "message": "Error while updating round",
                    "error": str(e),
                },
                ResCode.BAD_REQUEST.value,
            )
