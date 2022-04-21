from uuid import uuid4

from sanic.request import Request


async def prime_request_context(request: Request):
    request.ctx.trace_id = str(uuid4())
