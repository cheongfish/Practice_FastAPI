import datetime
from typing import List
from typing import Optional

from fastapi import FastAPI
from fastapi import HTTPException
from fastapi import status
from pydantic import BaseModel

app = FastAPI()

# define data models & tmp data

temp_data = {}
todo_counter = 0


# Set request data model
class Todo(BaseModel):
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


@app.get("/")
def hello():
    return {"message": "hello this page is root page"}


@app.post(path="/todos", response_model=Todo, status_code=status.HTTP_201_CREATED)
async def create_todo(todo_in: TodoCreate):
    global todo_counter
    todo_counter += 1
    new_todo = Todo(
        id=todo_counter,
        title=todo_in.title,
        description=todo_in.description,
        created_at=datetime.datetime.now(),
    )
    temp_data[new_todo.id] = new_todo  # insert data to temp data
    return new_todo


@app.get(path="/todos", response_model=List[Todo], status_code=status.HTTP_200_OK)
async def read_all_todo(skip: int = 0, limit: int = 10, completed: bool | None = None):
    all_todos = list(temp_data.values())
    # if param completed is not none filtering temp data
    if completed:
        all_todos = [todo for todo in all_todos if todo.completed == completed]

    return all_todos[: skip + limit]


@app.get(
    path="/todos/{todo_id}",
    response_model=Todo,
)
async def read_todo(
    todo_id,
):
    if todo_id not in temp_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"This {todo_id} is not in saved Todos Please check todo_id",
        )
    result = temp_data.get(todo_id)
    return result


@app.put(
    path="/todos/{todo_id}",
    response_model=Todo,
)
async def update_todo(
    todo_id,
    todo_in: TodoUpdate,
):
    if todo_id not in temp_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    stored_todo = temp_data.get(todo_id)
    update_data = todo_in.model_dump(exclude_unset=True)  # 입력된 필드만 가져옴
    # Pydantic 모델의 copy(update=...) 사용 (v2 이상)
    updated_todo = stored_todo.model_copy(update=update_data)
    temp_data[todo_id] = updated_todo
    return updated_todo


@app.delete(path="/todos/{todo_id}", status_code=status.HTTP_200_OK)
async def delete_todo(todo_id: int):
    if todo_id not in temp_data:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Todo not found"
        )
    del temp_data[todo_id]
    return {"message": "Todo deleted successfully"}
    # 또는 return {"message": "Todo deleted successfully"} 와 status_code=200 사용
