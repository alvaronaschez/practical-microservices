from sanic import Sanic


from .handlers import CustomErrorHandler


def mount_error_handlers(app: Sanic):
    app.error_handler = CustomErrorHandler()
