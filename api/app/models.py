from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    email: str
    avatar_url: str
    job_title: str
    company: str


class Product(BaseModel):
    id: int
    name: str
    description: str
    price: float
    image_url: str
    category: str
    in_stock: bool


class TaskBase(BaseModel):
    title: str
    description: str = ""
    completed: bool = False
    priority: str = "medium"


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    title: str | None = None
    description: str | None = None
    completed: bool | None = None
    priority: str | None = None


class Task(TaskBase):
    id: int
