from uuid import uuid4

from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, text


app = Sanic("MyApp")


@app.middleware("request")
async def prime_request_context(request: Request):
    request.ctx.traceId = uuid4()


@app.get("/")
async def hello_world(request: Request) -> HTTPResponse:
    return text("Hello, world")
