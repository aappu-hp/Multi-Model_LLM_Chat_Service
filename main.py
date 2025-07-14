from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import time
import json
import uvicorn
import os
from langchain_ollama.llms import OllamaLLM

app = FastAPI()

models = {
    "gemma3": OllamaLLM(model="gemma3:1b"),
    "tinyllama": OllamaLLM(model="tinyllama")
}

LOG_FILE = "logs.json"

def load_logs():
    if not os.path.isfile(LOG_FILE):
        return []
    try:
        with open(LOG_FILE, "r") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_logs(data):
    with open(LOG_FILE, mode="w") as f:
        json.dump(data, f, indent=2)

class PromptRequest(BaseModel):  
    prompt: str
    model: str  

@app.post("/chat")
async def chat(request: PromptRequest):
    model = request.model.lower()
    if model not in models:
        raise HTTPException(status_code=400, detail=f"Unsupported model '{model}'")
    llm = models[model]

    start = time.perf_counter()
    response = llm.invoke(request.prompt)
    latency_ms = (time.perf_counter() - start) * 1000

    token_count = len(request.prompt.split()) + len(response.split())

    log_entry = {
        "timestamp": time.strftime("%Y-%m-%dT%H:%M:%S", time.localtime()),
        "model": model,
        "prompt": request.prompt,
        "response": response,
        "latency_ms": round(latency_ms, 2),
        "token_count": token_count
    }

    logs = load_logs()
    logs.append(log_entry)
    save_logs(logs)

    return {
        "model": model,
        "response": response,
        "latency_ms": round(latency_ms, 2),
        "token_count": token_count
    }


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
