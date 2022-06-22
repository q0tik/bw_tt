import os

from pydantic import BaseSettings


class Config(BaseSettings):
    ENV: str = "development"
    DEBUG: bool = True
    APP_HOST: str = "0.0.0.0"
    APP_PORT: int = 8000
    WRITER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"
    READER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"
    CELERY_BROKER_URL: str = f"amqp://guest:guest@rabbitmq_tt:5672/vhost"
    CELERY_BACKEND_URL: str = "redis://:redis@redis_tt:6379/0"
    JWT_SECRET_KEY: str = "fastapi"
    JWT_ALGORITHM: str = "HS256"
    SENTRY_SDN: str = None


class DevelopmentConfig(Config):
    WRITER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"
    READER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"


class LocalConfig(Config):
    WRITER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"
    READER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"


class ProductionConfig(Config):
    DEBUG: str = False
    WRITER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"
    READER_DB_URL: str = f"postgresql+asyncpg://black_wall_user:black_wall_pwd@db_postgres/black_wall"


def get_config():
    env = os.getenv("ENV", "local")
    config_type = {
        "development": DevelopmentConfig(),
        "local": LocalConfig(),
        "production": ProductionConfig(),
    }
    return config_type[env]


config: Config = get_config()
