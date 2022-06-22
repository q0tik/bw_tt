from pydantic import BaseModel, Field


class CreateUserRequestSchema(BaseModel):
    email: str = Field(..., description="Email")
    first_name: str = Field(..., description="First_name")
    last_name: str = Field(..., description="Last_name")


class CreateUserResponseSchema(BaseModel):
    email: str = Field(..., description="Email")

    class Config:
        orm_mode = True


class UpdateUserBalanceResponseSchema(BaseModel):
    status: str = Field(..., description="Status")

    class Config:
        orm_mode = True


class UpdateUserBalanceRequestSchema(BaseModel):
    user_id: int = Field(..., description="User_id")
    balance_delta: int = Field(..., description="Balance_delta")

    class Config:
        orm_mode = True
