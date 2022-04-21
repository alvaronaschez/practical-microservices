from sanic.request import Request
from sanic.response import BaseHTTPResponse


# same as attach_locals but the way sanic documentation
# describes how to do it
# https://sanic.dev/en/guide/basics/headers.html#response
async def add_request_id_header(request: Request, response: BaseHTTPResponse):
    response.headers["X-Request-ID"] = request.id
