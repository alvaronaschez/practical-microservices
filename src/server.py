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


app = Sanic("MyApp", log_config=LOGGING_CONFIG)


@app.middleware("request")
async def prime_request_context(request: Request):
    request.ctx.trace_id = str(uuid4())


# # TODO: this makes little sense here: rethink this
# @app.middleware("response")
# async def attach_locals(request: Request, response: HTTPResponse):
#     setattr(response, "locals", {"context": request.ctx})


# sanic way to implement book's "lastResortErrorHandler" middleware
class CustomErrorHandler(ErrorHandler):
    def default(self, request, exception):
        """handles errors that have no error handlers assigned"""
        # You custom error handling logic...
        trace_id = request.ctx.trace_id if hasattr(request.ctx, "trace_id") else "None"
        msg = f'trace_id = "{trace_id}"\n{repr(exception)}'
        error_logger.error(msg)
        return super().default(request, exception)


@app.get("/")
async def hello_world(request: Request) -> HTTPResponse:
    # i = 1 / 0
    return json({"message": "Hello, world", "context": request.ctx.trace_id})


app.error_handler = CustomErrorHandler()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True, auto_reload=True, access_log=True)
