from sanic.request import Request
from sanic.response import BaseHTTPResponse


# from the book
async def attach_locals(request: Request, response: BaseHTTPResponse):
    response.headers["locals"] = {"ctx": vars(request.ctx)}
