from abc import ABC
from flask import Response, make_response

from backend.abstract.response_codes import ResCode


class Router(ABC):
    @staticmethod
    def handle_preflight_request() -> Response:
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, DELETE, OPTIONS, PATCH",
        )
        return response

    @staticmethod
    def handle_bad_request() -> Response:
        return make_response(
            {"message": "Bad request"}, ResCode.BAD_REQUEST.value
        )
