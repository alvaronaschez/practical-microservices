from sanic.request import Request
from sanic.response import HTTPResponse, json


async def hello_world(request: Request) -> HTTPResponse:
    return json({"message": "Hello, world", "context": request.ctx.trace_id})
