from pydantic import BaseModel

class User(BaseModel):
    name: str
    email: str
    password: str

class Answer(BaseModel):
    question: str
    answer: str

class InterviewRequest(BaseModel):
    role: str