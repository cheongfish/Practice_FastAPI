import datetime
from typing import Optional

from pydantic import BaseModel


# Set request data model
class TOdo(BaseModel):
    id: int  # 고유 ID
    title: str  # 할 일 제목
    description: Optional[str] = None  # 상세 설명 (선택)
    completed: bool = False  # 완료 여부 (기본값: False)
    created_at: datetime.datetime  # 생성시간


# 할 일 생성을 위한 요청 모델 (ID는 서버에서 생성함)
class TodoCreate(BaseModel):
    title: str
    description: Optional[str] = None  # 상세 설명 (선택)


# 할 일 수정을 위한 요청 모델
class TodoUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    completed: Optional[bool] = None


temp_data = {}
todo_counter = 0
