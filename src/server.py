from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json
from sanic.handlers import ErrorHandler
from sanic.log import LOGGING_CONFIG_DEFAULTS, error_logger


from middleware import mount_middleware


LOGGING_CONFIG = LOGGING_CONFIG_DEFAULTS

LOGGING_CONFIG["handlers"]["file"] = {
    "class": "logging.FileHandler",
    "filename": "logs/practical-microservices.log",
    "formatter": "generic",
}
LOGGING_CONFIG["loggers"]["sanic.error"]["handlers"].append("file")


app = Sanic("practical-microservices", log_config=LOGGING_CONFIG)

mount_middleware(app)


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
    return json({"message": "Hello, world", "context": request.ctx.trace_id})


app.error_handler = CustomErrorHandler()
app.ctx.host = "0.0.0.0"
app.ctx.port = 8000
app.ctx.debug = True
app.ctx.auto_reload = True
app.ctx.access_log = True


if __name__ == "__main__":
    app.run()
