from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy import Column, String, BigInteger, DateTime

from exporting_collector.models.abstract import TimestampBase


class PlatformSettings(TimestampBase):
    __tablename__ = "platform_settings"

    key = Column(String(128))
    value = Column(JSONB)
    updated_at = Column(DateTime, nullable=False)
    created_by = Column(BigInteger)
