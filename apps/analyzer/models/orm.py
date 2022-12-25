from __future__ import annotations

import datetime

from sqlalchemy import INT, Integer, String, JSON, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import functions

from models.base_model import BaseSqlModel


class AnalyzedData(BaseSqlModel):
    __tablename__ = 'analyzed_data'

    analyzed_data_id: Mapped[int] = mapped_column(
            Integer, 
            autoincrement=True,
            primary_key=True, 
            nullable=False,
        )
    object_raw: Mapped[dict] = mapped_column(JSON, nullable=False)


class AnalyzedMetadata(BaseSqlModel):
    __tablename__ = 'analyzed_metadata'

    analyzed_metadata_id: Mapped[int] = mapped_column(
            Integer, 
            primary_key=True,
        )
    analyzed_data_id: Mapped[int] = mapped_column(
            Integer,
            ForeignKey('analyzed_data.analyzed_data_id')
        )
    severity: Mapped[str] = mapped_column(String, nullable=False)
    score: Mapped[int] = mapped_column(INT, nullable=False)
    date_created: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=functions.now())
