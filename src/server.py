from uuid import uuid4

from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, json


app = Sanic("MyApp")


@app.middleware("request")
async def prime_request_context(request: Request):
    request.ctx.traceId = str(uuid4())


@app.get("/")
async def hello_world(request: Request) -> HTTPResponse:
    return json({"message": "Hello, world", "context": request.ctx.traceId})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)
