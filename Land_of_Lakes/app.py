from flask import Flask

from .routes.main import main
from .routes.add import add


def create_app():
    app = Flask(__name__)

    app.register_blueprint(main)
    app.register_blueprint(add)

    return app
