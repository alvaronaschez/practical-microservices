from sanic import Sanic
from tortoise.contrib.sanic import register_tortoise


def mount_database(app: Sanic):
    register_tortoise(
        app,
        db_url="mysql://root:root@localhost/test",
        modules={"models": ["models"]},
        generate_schemas=True,
    )
