from sqlalchemy import Column, Enum, Integer
from sqlalchemy.dialects.postgresql import JSONB

from src.db.db_setup import Base


class Problem(Base):
    __tablename__ = "problems"

    id = Column("id", Integer, autoincrement=True, primary_key=True, nullable=False)
    difficulty = Column("difficulty", Enum, nullable=False)
    problem = Column("problem", JSONB, nullable=False)
