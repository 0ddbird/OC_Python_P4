from flask import (
    Flask,
)
from flask_cors import (
    CORS,
)
from .router import (
    register_routes,
)

app = Flask(__name__)
register_routes(app)
CORS(app)


if __name__ == "__main__":
    app.run(debug=True)
