from abc import ABC
from flask import Response, make_response


class Router(ABC):
    def handle_preflight_request() -> Response:
        response = make_response()
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add("Access-Control-Allow-Headers", "Content-Type")
        response.headers.add(
            "Access-Control-Allow-Methods",
            "GET, POST, PUT, DELETE, OPTIONS",
        )
        return response

    def handle_bad_request() -> Response:
        return make_response(
            {"message": "Bad request"}, ResCode.BAD_REQUEST.value
        )
