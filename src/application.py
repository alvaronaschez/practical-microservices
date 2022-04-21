from sanic import Sanic


def create_app() -> Sanic:
    app = Sanic("practical-microservices")
    return app
