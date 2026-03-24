from fastapi import APIRouter
from utils.ai import generate_questions, evaluate_answer
from database import interview_collection
from pydantic import BaseModel
from typing import List
from utils.ai import client

router = APIRouter()

class RoleRequest(BaseModel):
    role: str

@router.post("/start")
def start_interview(data: RoleRequest):
    questions = generate_questions(data.role)
    return {"questions": questions}


class AnswerItem(BaseModel):
    question: str
    answer: str

class SubmitRequest(BaseModel):
    answers: List[AnswerItem]

@router.post("/submit")
def submit_answers(data: SubmitRequest):
    results = []

    for item in data.answers:
        evaluation = evaluate_answer(item.question, item.answer)
        results.append(evaluation)

    return {"results" : results}

# class ChatRequest(BaseModel):
#     role: str
#     answer: str = ""

# @router.post("/next")
# def next_question(data: ChatRequest):

#     try:
#         prompt = f"""
# You are a professional HR interviewer.

# Role: {data.role}

# Ask ONE interview question.

# Rules:
# - Only ask ONE question
# - No headings
# - No numbering
# - No extra text
# - Just a clean question
# """
#         response = client.chat.completions.create(
#             model = "moonshotai/Kimi-K2.5",
#             messages = [{"role" : "user", "content" : prompt}],
#         )

#         text = response.choices[0].message.content.strip()

#         if not text or "?" not in text:
#             text = "Can you tell me about yourself?"

#     except Exception as e:
#         print("AI ERROR:", e)
#         text = "Okay. Can you tell me more about your experience?"

#     return{"messages" : text}