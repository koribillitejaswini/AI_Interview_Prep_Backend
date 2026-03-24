from fastapi import FastAPI
from routes import auth, interview
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(interview.router, prefix="/interview")

@app.get("/")
def home():
    return {"message": "PrepAI Backend Running 🚀"}