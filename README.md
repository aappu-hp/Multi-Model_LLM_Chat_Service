
# 🚀 Multi-Model LLM Chat Service

This project is a **Python-based FastAPI service** that integrates multiple open-source LLMs (e.g., `gemma3`, `tinyllama`) using the `langchain_ollama` library. The service accepts user prompts via HTTP, routes them to the selected model, and returns the model's response along with latency and token count. Logs are persisted in a JSON file for analysis.

---

## ✨ Features

1. ✅ **Multi-Model Support**: Route prompts to different models (e.g., `gemma3`, `tinyllama`) using the `model` parameter in the request body.
2. ⏱ **Latency and Token Logging**: Logs round-trip latency and token count for each request/response in a `logs.json` file.
3. 🌐 **Simple HTTP API**: Exposes a `/chat` endpoint to accept user prompts and return model responses.
4. 📁 **JSON Logging**: Logs are stored in a structured JSON format for easy analysis.

---

## 📁 Project Structure

```
.
├── .gitignore          # Specifies intentionally untracked files to ignore
├── .python-version     # Python version specification (if using pyenv)
├── README.md           # Project documentation (this file)
├── logs.json           # Persistent interaction logs (created after first run)
├── main.py             # FastAPI application entry point
├── pyproject.toml      # Python project metadata and build configuration
├── requirements.txt    # Python dependencies list
├── uv.lock             # UV package manager lock file
```
---

## 📦 Prerequisites

- 🐍 **Python**: Version 3.10 or higher  
- 📦 **UV Package Manager**: For creating a virtual environment and managing dependencies  
- 🧠 **Ollama**: A local LLM server required for running the models  
- 📥 **Models**: Ensure `gemma3`, `tinyllama` are pulled using the Ollama CLI

---

## ⚙️ Setup Instructions

### 1. 🧬 Clone the Repository
```bash
git clone https://github.com/aappu-hp/Multi-Model_LLM_Chat_Service.git
cd Multi-Model_LLM_Chat_Service
```

### 2. 🧪 Create a Virtual Environment
Use the `uv` package manager:
```bash
uv venv 
```

Activate the virtual environment:
- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
- **Linux/Mac**:
  ```bash
  source .venv/bin/activate
  ```

### 3. 📦 Install Dependencies
```bash
uv add -r requirements.txt
```

### 4. 🔧 Install Ollama
Download and install the Ollama CLI from [Ollama's official website](https://ollama.com/). Follow the installation instructions for your operating system.

### 5. 📥 Pull Required Models
```bash
ollama pull gemma3:1b
ollama pull tinyllama
```

Verify:
```bash
ollama list
```

### 6. ▶️ Start the Ollama Server
```bash
ollama serve
```

### 7. 🚀 Run the FastAPI Application
```bash
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

---

## 📡 API Usage

### 🔗 Endpoint: `/chat`

#### 📤 Request
- **Method**: `POST`
- **Content-Type**: `application/json`
- **Body**:
```json
{
  "prompt": "Your input prompt here",
  "model": "gemma3"
}
```

#### 📥 Response
- **Status Code**: `200 OK`
```json
{
  "model": "gemma3",
  "response": "Model's response here",
  "latency_ms": 123.45,
  "token_count": 42
}
```

#### ❌ Error Handling
- **Unsupported Model**:
```json
{
  "detail": "Unsupported model 'invalid_model'"
}
```

---

## 🧪 Testing

### 🧪 Using Thunder Client Extension
1. Install the [Thunder Client](https://marketplace.visualstudio.com/items?itemName=rangav.vscode-thunder-client)
2. Create a new `POST` request:
   - **URL**: `http://localhost:8000/chat`
   - **Headers**: `Content-Type: application/json`
   - **Body**:
     ```json
     {
       "prompt": "Hello, world!",
       "model": "gemma3"
     }
     ```
3. Send and verify the response.

### 🌐 Using FastAPI Swagger UI
- Visit: [http://localhost:8000/docs](http://localhost:8000/docs)
- Use the interactive Swagger UI to test the `/chat` endpoint

### 🧵 Using cURL
```bash
curl -X POST http://localhost:8000/chat ^
-H "Content-Type: application/json" ^
-d "{\"prompt\": \"Hello, world!\", \"model\": \"gemma3\"}"
```

---

## 🗃 Logging

Logs are stored in `logs.json` as:
```json
[
  {
    "timestamp": "2025-07-14T12:34:56",
    "model": "gemma3",
    "prompt": "Your input prompt here",
    "response": "Model's response here",
    "latency_ms": 123.45,
    "token_count": 42
  }
]
```

---

## 🛠️ Troubleshooting 🔍

| Issue                  | Solution                                               |
|------------------------|--------------------------------------------------------|
| ❌ Model not responding | ✅ Verify `ollama serve` is running                    |
| 🚫 Import errors        | 🔄 Recreate virtual environment with `uv venv`         |
| ⚠️ Unsupported model    | 🔍 Check `ollama list` for available models            |
| 🔌 Connection refused   | 🖥️ Ensure API is running on port `8000`               |