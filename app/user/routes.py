from litestar import Controller, get, post, put, delete
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.user.models import User
from app.user.schemas import UserCreate, UserRead, UserUpdate
from uuid import UUID


class UserController(Controller):
    """
    CRUD-операции с таблицей User
    """
    path = "/users"

    @post()
    async def create_user(self, data: UserCreate, db_session: AsyncSession) -> UserRead:
        user = User(name=data.name, email=data.email)
        db_session.add(user)
        await db_session.commit()
        await db_session.refresh(user)
        return UserRead.model_validate(user)

    @get()
    async def list_users(self, db_session: AsyncSession) -> list[UserRead]:
        result = await db_session.execute(select(User))
        users = result.scalars().all()
        return [UserRead.model_validate(user) for user in users]

    @get("/{user_id:uuid}")
    async def get_user(self, user_id: UUID, db_session: AsyncSession) -> UserRead:
        user = await db_session.get(User, user_id)
        if not user:
            raise ValueError("User not found")
        return UserRead.model_validate(user)

    @put("/{user_id:uuid}")
    async def update_user(self, user_id: UUID, data: UserUpdate, db_session: AsyncSession) -> UserRead:
        user = await db_session.get(User, user_id)
        if not user:
            raise ValueError("User not found")
        for attr, value in data.dict(exclude_unset=True).items():
            setattr(user, attr, value)
        await db_session.commit()
        await db_session.refresh(user)
        return UserRead.model_validate(user)

    @delete("/{user_id:uuid}")
    async def delete_user(self, user_id: UUID, db_session: AsyncSession) -> None:
        user = await db_session.get(User, user_id)
        if not user:
            raise ValueError("User not found")
        await db_session.delete(user)
        await db_session.commit()
