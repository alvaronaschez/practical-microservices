from sanic.handlers import ErrorHandler
from sanic.log import error_logger


# sanic way to implement book's "lastResortErrorHandler" middleware
class CustomErrorHandler(ErrorHandler):
    def default(self, request, exception):
        """handles errors that have no error handlers assigned"""
        # You custom error handling logic...
        trace_id = getattr(request.ctx, "trace_id", "")
        msg = f'trace_id = "{trace_id}"\n{repr(exception)}'
        error_logger.error(msg)
        return super().default(request, exception)
