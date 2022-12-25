from __future__ import annotations

import datetime

from sqlalchemy import INT, Integer, String, JSON, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql import functions

from models.base_model import BaseSqlModel
from models.analyzed_object import AnalyzedObject


class AnalyzedData(BaseSqlModel):
    __tablename__ = 'analyzed_data'

    analyzed_data_id: Mapped[int] = mapped_column(
            Integer, 
            autoincrement=True,
            primary_key=True, 
            nullable=False,
        )
    object_raw: Mapped[dict] = mapped_column(JSON, nullable=False)

    def __init__(self, local_analyzed_object: AnalyzedObject) -> None:
        self.object_raw = local_analyzed_object.original_object


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

    def __init__(self, local_analyzed_object: AnalyzedObject, analyzed_data: AnalyzedData) -> None:
        self.analyzed_data_id = analyzed_data.analyzed_data_id
        self.severity = local_analyzed_object.severity
        self.score = local_analyzed_object.severity_score
