from flask import make_response


def handle_preflight_request():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", "*")
    response.headers.add("Access-Control-Allow-Headers", "Content-Type")
    response.headers.add(
        "Access-Control-Allow-Methods", "GET, POST, PUT, DELETE, OPTIONS"
    )
    return response


def api_response(status, status_code, payload=None):
    return {"status": status, "status_code": status_code, "payload": payload}
