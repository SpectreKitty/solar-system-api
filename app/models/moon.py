from sqlalchemy.orm import Mapped, mapped_column, relationship
from ..db import db
from sqlalchemy import ForeignKey
from typing import Optional, TYPE_CHECKING

class Moon(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str]
    size: Mapped[int]
    description: Mapped[str]

    planet_id: Mapped[Optional[int]] = mapped_column(ForeignKey("planet.id"))
    planet: Mapped[Optional["Planet"]] = relationship(back_populates="planets")

    if TYPE_CHECKING:
        from .planets import Planet
        