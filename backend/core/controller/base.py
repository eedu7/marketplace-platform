from typing import Any, Dict, Generic, Sequence, Type, TypeVar
from uuid import UUID

from core.database import DBBase
from core.exceptions.base import NotFoundException
from core.repository import BaseRepository

ModelType = TypeVar("ModelType", bound=DBBase)


class BaseController(Generic[ModelType]):
    def __init__(self, model: Type[ModelType], repository: BaseRepository) -> None:
        self.model = model
        self.repository = repository

    async def get_by_uid(self, uid: UUID) -> ModelType:
        obj = await self.repository.get_by_uid(uid)

        if obj is None:
            raise NotFoundException(
                f"{self.model.__name__} with uid {uid} not found",
            )
        return obj

    async def get_all(self, offset: int = 0, limit: int = 100) -> Sequence[ModelType]:
        return await self.repository.get_all(offset=offset, limit=limit)

    async def create(self, attributes: Dict[str, Any]) -> ModelType:
        create = await self.repository.create(attributes=attributes)
        await self._commit()
        return create

    async def delete(self, model: ModelType) -> bool:
        delete = await self.repository.delete(model)
        await self._commit()
        return delete

    async def _commit(self) -> None:
        await self.repository.session.commit()
