from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json

from application import create_app, run_app

app: Sanic = create_app()


async def hello_world(request: Request) -> HTTPResponse:
    return json({"message": "Hello, world", "context": request.ctx.trace_id})


app.add_route(hello_world, "/", ("GET",))


configuration = dict(
    host="0.0.0.0",
    port=8000,
    debug=True,
    auto_reload=True,
    access_log=True,
)

if __name__ == "__main__":
    run_app(app, configuration)
