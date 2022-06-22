from typing import Optional, List, Union, NoReturn

from sqlalchemy import select
import aio_pika

from app.user.models import User
from core.db import Transactional, Propagation, session
from core.exceptions import (
    NoSuchUserException,
    DuplicateEmailException,
    NotEnoughMoneyBitchException,
)


class UserService:
    def __init__(self):
        pass

    @Transactional(propagation=Propagation.REQUIRED)
    async def update_balance(
        self,
        user_id: int,
        balance_delta: int
    ) -> None:
        result = await session.execute(
            select(User).where(User.id == user_id)
        )
        user = result.scalars().first()
        if not user:
            raise NoSuchUserException

        if user.balance_rub + balance_delta < 0:
            raise NotEnoughMoneyBitchException

        user.balance_rub += balance_delta

        session.add(user)

    @Transactional(propagation=Propagation.REQUIRED)
    async def create_user(
        self, email: str, first_name: str, last_name: str
    ) -> None:

        result = await session.execute(
            select(User).where(User.email == email)
        )
        is_exist = result.scalars().first()
        if is_exist:
            raise DuplicateEmailException

        user = User(
            email=email,
            balance_rub=0,
            first_name=first_name,
            last_name=last_name
        )
        session.add(user)
