import sys

from loguru import logger

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from api.applications import create_application, get_applications
from database.db import get_db
from kafka.producer import publish_to_kafka
from api.schemas import ApplicationList, ApplicationCreate

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time} {level} {message}", backtrace=True, diagnose=True)


router = APIRouter()


@router.post("/applications", response_model=ApplicationList)
async def create_new_application(
    application: ApplicationCreate,
    session: AsyncSession = Depends(get_db)
):
    new_app = await create_application(session, application)
    await publish_to_kafka(new_app)
    return new_app


@router.get("/applications", response_model=list[ApplicationList])
async def list_applications(
    user_name: str = None,
    page: int = 1,
    size: int = 10,
    session: AsyncSession = Depends(get_db)
):
    return await get_applications(session, user_name, page, size)