# AI Technical Translator Pro

A web application that translates technical or complex text into clear, easy-to-understand language. Supports four explanation modes: **simple**, **ELI5**, **professional non-technical**, and **analogy-based**.

## Tech Stack

- **Backend:** FastAPI, Uvicorn, OpenAI API (GPT-3.5-turbo), Pydantic, python-dotenv
- **Frontend:** Vue 3 + Vite, Fetch API, Bootstrap

## Running without Docker (Development)

### Backend

```bash
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Edit .env and add your OpenAI API key
uvicorn main:app --reload --port 8000
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

The frontend will be available at http://localhost:5173 and the backend API at http://localhost:8000.

### Health check

```
GET http://localhost:8000/health
```

## Running with Docker

```bash
cp backend/.env.example backend/.env
# Add your OpenAI API key to backend/.env
docker-compose up
```

App available at http://localhost:8080.
