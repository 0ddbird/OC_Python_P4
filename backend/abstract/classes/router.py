from abc import ABC
from flask import Response, make_response

from backend.abstract.response_codes import ResCode


class Router(ABC):
    @staticmethod
    def handle_bad_request() -> Response:
        return make_response(
            {"message": "Bad request"}, ResCode.BAD_REQUEST.value
        )
