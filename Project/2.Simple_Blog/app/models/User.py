from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime


class User:
    """
    Define User table
    display User of 게시판 시스템
    """

    __table_name__ = "users"  # table name
    # Set columns

    # User unique id, primary key, create index
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    # Hashed password not null
    hashed_password = Column(
        String,
        nullable=False,
        index=True,
    )
    # Is actived user , default is True
    is_active = Column(
        Boolean,
        default=True,
    )
    # Is superuser, default is False
    is_superuser = Column(
        Boolean,
        default=False,
    )
    # Created time
    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now(),
    )
    # Last updated time
    update_at = Column(
        DateTime(timezone=True),
        onupdate=func.now(),
    )

    # set relationship
    posts = relationship("Post", back_populates="owner")

    def __repr__(self) -> str:
        """
        Use when represention instance to string


        Returns:
            str: _description_
        """
        return f"<User(id={self.id})"
