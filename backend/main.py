from fastapi import FastAPI

app = FastAPI()

@app.post("/generate")
def generate():
    return {"status": "ok"}

@app.get("/status/{id}")
def status(id: int):
    return {"id": id, "status": "pending"}
