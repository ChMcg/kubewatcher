from __future__ import annotations

import datetime

from sqlalchemy import INT, String, JSON, DateTime
from sqlalchemy import Sequence, ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from sqlalchemy.sql import functions

from models.base_model import BaseSqlModel


class AnalyzedData(BaseSqlModel):
    __tablename__ = 'analyzed_data'

    analyzed_data_id: Mapped[int] = mapped_column(
            INT, 
            Sequence('analyzed_data_id'), 
            autoincrement=True,
            primary_key=True, 
            nullable=False,
        )
    object_raw: Mapped[dict] = mapped_column(JSON, nullable=False)
    metadata_id: Mapped[int] = relationship(back_populates='analyzed_metadata_id')


class AnalyzedMetadata(BaseSqlModel):
    __tablename__ = 'analyzed_metadata'

    analyzed_metadata_id: Mapped[int] = mapped_column(
            INT, 
            Sequence('analyzed_metadata_id'),
            autoincrement=True,
            primary_key=True,
            nullable=False
        )
    analyzed_data_id: Mapped[int] = mapped_column(
            ForeignKey('analyzed_data.analyzed_data_id')
        )
    severity: Mapped[str] = mapped_column(String, nullable=False)
    score: Mapped[int] = mapped_column(INT, nullable=False)
    date_created: Mapped[datetime.datetime] = mapped_column(DateTime(timezone=True), server_default=functions.now())
    analyzed_data: Mapped[dict] = relationship(back_populates='object_raw')
