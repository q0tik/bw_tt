from sqlalchemy import Column, Unicode, BigInteger

from core.db import Base
from core.db.mixins import TimestampMixin


class User(Base, TimestampMixin):
    __tablename__ = "users"

    id = Column(BigInteger, primary_key=True, autoincrement=True)
    balance_rub = Column(BigInteger, nullable=False)
    email = Column(Unicode(255), nullable=False, unique=True)
    first_name = Column(Unicode(255), nullable=False, unique=True)
    last_name = Column(Unicode(255), nullable=False, unique=True)

