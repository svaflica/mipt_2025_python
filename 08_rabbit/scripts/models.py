from sqlalchemy import String, Boolean
from sqlalchemy.orm import declarative_base, Mapped, mapped_column
from sqlalchemy import ForeignKey


Base = declarative_base()


class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String, index=True)
    password: Mapped[str] = mapped_column(String)
