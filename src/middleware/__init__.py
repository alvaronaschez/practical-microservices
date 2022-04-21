from sanic import Sanic


from .prime_request_context import prime_request_context
from .attach_locals import attach_locals
from .add_request_id_header import add_request_id_header


def mount_middleware(app: Sanic):
    app.register_middleware(prime_request_context, "request")
    app.register_middleware(attach_locals, "response")
    app.register_middleware(add_request_id_header, "response")
