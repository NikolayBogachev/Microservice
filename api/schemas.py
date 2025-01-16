from datetime import datetime

from pydantic import BaseModel


class TunedModel(BaseModel):
    """
    Базовый класс для всех моделей.
    Конфигурация:
    - from_attributes: позволяет создавать модели из словарей атрибутов.
    """

    class Config:
        from_attributes = True


class ApplicationCreate(TunedModel):
    user_name: str
    description: str


class ApplicationList(TunedModel):
    id: int
    user_name: str
    description: str
    created_at: datetime

