from pydantic import BaseSettings


class Settings(BaseSettings):

    KAFKA_BOOTSTRAP_SERVER: str = "localhost:9092"
    KAFKA_GROUP_ID: int = 0
    TOPIC_CONSUME_EVENTS: str = "test"
    CSRF_ENABLED: bool = True
    SESSION_COOKIE_SECURE: bool = True

    SYSLOG_HOST: str = "localhost"
    SYSLOG_PORT: int = 5432

    APP_POSTGRESQL_HOST: str = "localhost"
    APP_POSTGRESQL_PASSWORD: str = "password"
    APP_POSTGRESQL_USER: str = "username"
    APP_POSTGRESQL_NAME: str = "db"
    APP_POSTGRESQL_PORT: int = 5432

    class Config:
        env_file = "./.env"


settings = Settings()
