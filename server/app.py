from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/reset")
def reset():
    return {"status": "reset successful"}

@app.get("/")
def home():
    return {"message": "API running"}

def main():
    uvicorn.run(app, host="0.0.0.0", port=7860)