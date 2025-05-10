from litestar import Litestar
from litestar.openapi import OpenAPIConfig
from app.user.routes import UserController
from app.db import alchemy_plugin

app = Litestar(
    plugins=[alchemy_plugin],
    route_handlers=[UserController],
    openapi_config=OpenAPIConfig(
        title="Litestar",
        version="1.0.0",
        description="REST API на базе LiteStar (Python 3.12) с CRUD-операциями для таблицы user в PostgreSQL"
    ))
