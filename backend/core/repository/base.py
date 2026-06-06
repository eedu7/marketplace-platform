from typing import Any, Dict, Generic, Sequence, Type, TypeVar
from uuid import UUID

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from core.database import DBBase

ModelType = TypeVar("ModelType", bound=DBBase)


class BaseRepository(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        self.model = model
        self.session = session

    async def create(self, attributes: Dict[str, Any] | None = None) -> ModelType:
        if attributes is None:
            attributes = {}
        instance = self.model(**attributes)
        self.session.add(instance)
        return instance

    async def get_by_uid(self, uid: UUID) -> ModelType | None:
        return await self.session.get(self.model, uid)

    async def get_all(self, offset: int = 0, limit: int = 100) -> Sequence[ModelType]:
        query = select(self.model).offset(offset).limit(limit)
        result = await self.session.execute(query)
        return result.scalars().all()

    async def get_by(self, field: str, value: Any) -> ModelType | None:
        query = select(self.model).where(getattr(self.model, field) == value)
        result = await self.session.execute(query)
        return result.scalars().first()

    async def delete(self, model: ModelType) -> bool:
        await self.session.delete(model)
        return True
