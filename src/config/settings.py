from pydantic import BaseSettings


class Settings(BaseSettings):

    KAFKA_HOST: str = "localhost:9092"
    KAFKA_GROUP_ID: int = 0
    TOPIC_CONSUME_EVENTS: str = ""

    SYSLOG_HOST: str = "localhost"
    SYSLOG_PORT: int = "543"

    class Config:
        env_file = "./.env"


settings = Settings()
