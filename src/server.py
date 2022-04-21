from uuid import uuid4

from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic.handlers import ErrorHandler
from sanic.log import LOGGING_CONFIG_DEFAULTS, error_logger

LOGGING_CONFIG = LOGGING_CONFIG_DEFAULTS

LOGGING_CONFIG["handlers"]["file"] = {
    "class": "logging.FileHandler",
    "filename": "logs/practical-microservices.log",
    "formatter": "generic",
}
LOGGING_CONFIG["loggers"]["sanic.error"]["handlers"].append("file")


app = Sanic("practical-microservices", log_config=LOGGING_CONFIG)


async def prime_request_context(request: Request):
    request.ctx.trace_id = str(uuid4())


app.register_middleware(prime_request_context, "request")


# from the book
async def attach_locals(request: Request, response: HTTPResponse):
    response.headers["locals"] = {"ctx": vars(request.ctx)}


app.register_middleware(attach_locals, "response")


# same as attach_locals but the way sanic documentation
# describes how to do it
# https://sanic.dev/en/guide/basics/headers.html#response
async def add_request_id_header(request, response):
    response.headers["X-Request-ID"] = request.id


app.register_middleware(add_request_id_header, "response")


# sanic way to implement book's "lastResortErrorHandler" middleware
class CustomErrorHandler(ErrorHandler):
    def default(self, request, exception):
        """handles errors that have no error handlers assigned"""
        # You custom error handling logic...
        trace_id = getattr(request.ctx, "trace_id", "")
        msg = f'trace_id = "{trace_id}"\n{repr(exception)}'
        error_logger.error(msg)
        return super().default(request, exception)


@app.get("/")
async def hello_world(request: Request) -> HTTPResponse:
    # i = 1 / 0
    return json({"message": "Hello, world", "context": request.ctx.trace_id})


app.error_handler = CustomErrorHandler()


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=8000,
        debug=True,
        auto_reload=True,
        access_log=True
    )
