from sanic import Sanic


from logging_ import CONFIG
from middleware import mount_middleware
from error_handling import mount_error_handlers


def create_app() -> Sanic:
    app = Sanic("practical-microservices", log_config=CONFIG)
    mount_middleware(app)
    mount_error_handlers(app)
    return app


def run_app(app: Sanic, configuration: dict):
    app.run(**configuration)
