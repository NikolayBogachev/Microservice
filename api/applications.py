from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from database.models import Application
from api.schemas import ApplicationCreate


async def create_application(session: AsyncSession, application_data: ApplicationCreate) -> Application:
    new_app = Application(**application_data.dict())
    session.add(new_app)
    await session.commit()
    await session.refresh(new_app)
    return new_app


async def get_applications(session: AsyncSession, user_name: str, page: int, size: int):
    query = select(Application)
    if user_name:
        query = query.where(Application.user_name == user_name)
    result = await session.execute(query.offset((page - 1) * size).limit(size))
    return result.scalars().all()