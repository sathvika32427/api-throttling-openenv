from fastapi import FastAPI
from baseline.run_agent import run_episode

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/run")
def run():
    score = run_episode()
    return {"score": score}