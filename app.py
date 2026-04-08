from fastapi import FastAPI
import subprocess

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.get("/")
def home():
    return {"message": "API running"}

@app.get("/run")
def run():
    result = subprocess.run(["python", "inference.py"], capture_output=True, text=True)
    return {"output": result.stdout}