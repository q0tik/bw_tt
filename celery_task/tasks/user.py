import asyncio

from app.user.services import UserService
from .. import celery_app


@celery_app.task(name="update_user_balance")
def update_user_balance_task(user_id: int, balance_delta: int):
    asyncio.run(UserService().update_balance(user_id, balance_delta))
