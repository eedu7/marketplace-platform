from uuid import UUID, uuid4

from sqlalchemy import UUID as PG_UUID
from sqlalchemy import Unicode
from sqlalchemy.orm import Mapped, mapped_column

from core.database import DBBase


class DBUser(DBBase):
    __tablename__ = "users"

    uid: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        index=True,
        nullable=False,
        unique=True,
        default=uuid4,
    )
    email: Mapped[str] = mapped_column(Unicode(255), nullable=False, unique=True)
    username: Mapped[str] = mapped_column(Unicode(255), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(Unicode(255), nullable=False)

    def __repr__(self) -> str:
        return f"DBUser(uid={self.uid}, email={self.email}, username={self.username})"

    def __str__(self) -> str:
        return f"DBUser(uid={self.uid}, email={self.email}, username={self.username})"
