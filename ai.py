from openai import OpenAI
import os 
from dotenv import load_dotenv

load_dotenv(override = True)


client = OpenAI(api_key = "GoA3Fg6Z.QukwIrixtYoXvXxZGErpcrptYLxSRFRq", 
                base_url = "https://inference.baseten.co/v1")


def generate_questions(role):
    prompt = f"""
    Generate exactly 5 interview questions for {role}.

    STRICT RULES:
    - Do NOT include headings
    - Do NOT include separators like ---
    - Do NOT number questions
    - Do NOT include titles like "Technical Questions"
    - Return ONLY questions
    - Each question must be on a new line"""

    response = client.chat.completions.create(
        model = "moonshotai/Kimi-K2.5",
        messages = [{"role" : "user", "content" : prompt}]
    )

    content = response.choices[0].message.content
    return content.split("\n")


def evaluate_answer(question, answer):
    prompt = f"""
    Evaluate this answer:
    Question: {question}
    Answer: {answer}

    Give:
    -Score out of 10
    -Strength
    -Improvement
    """

    response = client.chat.completions.create(
        model = "moonshotai/Kimi-K2.5",
        messages = [{"role" : "user", "content" : prompt}]
    )

    return response.choices[0].message.content 
