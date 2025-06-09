from sqlalchemy import Boolean
from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.types import DateTime


class Post:
    """
    Define post table
    """

    __table_name__ = "posts"  # table name
    # Set columns

    # User unique id, primary key, create index
    id = Column(
        Integer,
        primary_key=True,
        index=True,
    )
    # user_id (Fk, UUID , Not Null)
    user_id = Column(
        Integer,
        nullable=False,
    )
    # title
    title = Column(
        String,
        nullable=False,
    )
    content = Column(
        String,
        nullable=False,
    )
    category_id = Column(
        Integer,
        nullable=False,
    )
    views = Column(
        Integer,
        default=0,
    )
    is_published = Column(Boolean, default=True)
    # 초안일 경우 Null
    published_at = Column(
        DateTime,
        nullable=False,
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
    categories = relationship("category", back_populates="id")

    def __repr__(self) -> str:
        """
        Use when represention instance to string


        Returns:
            str: _description_
        """
        return f"<User(id={self.id})"
