from sanic.log import LOGGING_CONFIG_DEFAULTS


CONFIG = LOGGING_CONFIG_DEFAULTS

CONFIG["handlers"]["file"] = {
    "class": "logging.FileHandler",
    "filename": "logs/practical-microservices.log",
    "formatter": "generic",
}
CONFIG["loggers"]["sanic.error"]["handlers"].append("file")
