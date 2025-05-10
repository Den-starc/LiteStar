import os

from sqlalchemy.orm import declarative_base
from advanced_alchemy.extensions.litestar import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

alchemy_config = SQLAlchemyAsyncConfig(
    connection_string=os.getenv("DATABASE_URL"),
    session_dependency_key="db_session",
)

alchemy_plugin = SQLAlchemyPlugin(config=alchemy_config)
