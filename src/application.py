from sanic import Sanic

from logging_ import CONFIG
from middleware import mount_middleware
from error_handling import mount_error_handlers
from database import mount_database
from handlers import hello_world


def create_app() -> Sanic:
    app = Sanic("practical-microservices", log_config=CONFIG)
    mount_middleware(app)
    mount_error_handlers(app)
    mount_database(app)
    app.add_route(hello_world, "/", ("GET",))
    return app


def run_app(app: Sanic, configuration: dict):
    app.run(**configuration)
