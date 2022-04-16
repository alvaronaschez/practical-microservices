from sanic import Sanic
from sanic.request import Request
from sanic.response import HTTPResponse, text


app = Sanic("MyApp")


@app.get("/")
async def hello_world(request: Request) -> HTTPResponse:
    return text("Hello, world")
