from pydantic import BaseModel
from typing import List

class Task(BaseModel):
    name: str
    priority: int
    deadline: int = 1
    duration: int = 1

class Observation(BaseModel):
    tasks: List[Task]

class Action(BaseModel):
    task_index: int

class Reward(BaseModel):
    score: float