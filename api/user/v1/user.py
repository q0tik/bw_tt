from fastapi import APIRouter

from app.user.schemas import (
    ExceptionResponseSchema,

    UpdateUserBalanceResponseSchema,
    UpdateUserBalanceRequestSchema,

    CreateUserRequestSchema,
    CreateUserResponseSchema,
)
from app.user.services import UserService

# from celery_task.tasks import update_user_balance_task

user_router = APIRouter()


@user_router.post(
    "",
    response_model=CreateUserResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def create_user(request: CreateUserRequestSchema):
    await UserService().create_user(**request.dict())
    return {"email": request.email}


@user_router.patch(
    "/update_balance",
    response_model=UpdateUserBalanceResponseSchema,
    responses={"400": {"model": ExceptionResponseSchema}},
)
async def update_balance(request: UpdateUserBalanceRequestSchema):
    await UserService().update_balance(**request.dict())
    # update_user_balance_task.apply_async(queue=f'user_update_balance_{request.user_id}', kwargs=request.dict())
    return {"status": "ok"}
