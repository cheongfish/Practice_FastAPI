from database import Base
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String

# 1. 할 일 목록의 데이터를 담을 데이터 모델 설계하기
"""
|      id     | todo id   |
|     name    | todo name |
| description | todo desc |
| create_date | created time todo|
"""


class Todo(Base):
    __tablename__ = "todo"

    id = Column(Integer, primary_key=True)
    name = Column(String, primary_key=False)
    description = Column(String, primary_key=False, nullable=True)
    create_date = Column(DateTime, primary_key=False)
