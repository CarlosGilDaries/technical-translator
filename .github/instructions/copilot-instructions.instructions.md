# AI Technical Translator Pro — Copilot Instruction & Progress Log

## 📌 Project Explanation (What, Why, How)

**What it does:**  
A web application that translates technical or complex text into clear, easy-to-understand language. Users can choose between different explanation modes: simple, ELI5 (Explain Like I'm 10), professional non-technical, or analogy-based.

**Why it solves a real problem:**  
Developers, managers, and students often struggle with jargon-heavy documentation, emails, or error messages. This tool makes technical knowledge accessible to anyone, regardless of their background.

**How AI is used:**  
The backend (FastAPI) sends the user's text and a mode-specific prompt to an LLM (OpenAI GPT-3.5-turbo). The AI returns a rewritten version adapted to the chosen audience. The frontend (Vue) provides a clean interface to input text, select a mode, and view the result.

**Development Principles:**

- All code must be written in English.
- Use explicit type hints for all functions.
- Follow PEP8 and prioritize readability.
- Write clear and consistent docstrings (pydoc style).
- Use self-explanatory naming.
- Avoid duplication and keep functions small (single responsibility).

---

## ⚙️ Tech Stack (fixed)

| Layer     | Technology                                                            |
| --------- | --------------------------------------------------------------------- |
| Backend   | FastAPI, Uvicorn, OpenAI API (GPT-3.5-turbo), Pydantic, python-dotenv |
| Frontend  | Vue 3 + Vite, Fetch API, Bootstrap                                    |
| Container | Docker + docker-compose                                               |
| Testing   | pytest (optional, but recommended)                                    |
| AI model  | OpenAI `gpt-3.5-turbo` (temperature=0.3)                              |

---

## 🏛️ Backend Architecture Rules (CRITICAL)

- main.py must ONLY:
  - create FastAPI app
  - register routers
  - configure middleware
- DO NOT define:
  - endpoints in main.py
  - business logic in main.py
  - Pydantic models in main.py

### Required folder structure:

- api/routes/ → API endpoints only
- services/ → business logic (AI calls, processing)
- models/ → Pydantic schemas
- core/ → configuration and environment variables

## Rules:

- All endpoints must be implemented using FastAPI routers (APIRouter)
- Each feature must be separated into its own module
- No business logic inside route handlers
- Route handlers must call service functions only

---

## 🤖 Copilot Responsibility (CRITICAL)

As the AI assistant, you (GitHub Copilot) are responsible for:

1. **Updating this `.md` file** as the project evolves.
2. **Marking tasks as `[x]`** when they are implemented.
3. **Adding a short description** of what was built in each phase (under "✅ Progress").
4. **Keeping this file as the single source of truth** for the roadmap and progress.
5. **Preserving the phase structure** (do not delete or reorder sections).

---

## 🚀 PHASE 1 — Project Setup

**Goal:** Initialize backend and frontend projects with proper structure.

### Tasks

- [x] Create repository and local folder structure (`backend/`, `frontend/`)
- [x] **Backend Python virtual environment (CRITICAL first step):**
  - Navigate to `backend/`
  - Run `python -m venv .venv`
  - Activate it:
    - Windows: `.venv\Scripts\activate`
    - macOS/Linux: `source .venv/bin/activate`
  - Add `.venv/` to `.gitignore`
- [x] Install backend dependencies **inside the activated virtual environment**:
      `pip install fastapi uvicorn openai python-dotenv pydantic`
- [x] Generate `backend/requirements.txt` with `pip freeze > requirements.txt`
- [x] Create `backend/main.py` with a health check endpoint (`GET /health`)
- [x] Initialize Vue 3 + Vite: `npm create vue@latest` (choose Vue 3, JavaScript, no TypeScript for speed)
- [x] Create `backend/.env.example` with `OPENAI_API_KEY=your_key_here`
- [x] Add `.gitignore` (ignore `.env`, `node_modules`, `__pycache__`, `.venv/`)
- [x] Create initial `README.md` with basic run instructions (without Docker first)

### ✅ Progress

- [x] Created `backend/` and `frontend/` folder structure.
- [x] Python virtual environment created at `backend/.venv` (Python 3.13).
- [x] Installed: fastapi==0.135.3, uvicorn==0.44.0, openai==2.31.0, python-dotenv==1.2.2, pydantic==2.13.0, pydantic-settings.
- [x] Generated `backend/requirements.txt` via `pip freeze`.
- [x] Created strict backend package structure: `api/routes/`, `services/`, `models/`, `core/`.
- [x] `main.py` refactored to only create the app, register routers, and configure CORS middleware.
- [x] `GET /health` moved to `api/routes/health.py` using `APIRouter`.
- [x] Pydantic models (`TranslationRequest`, `TranslationResponse`) moved to `models/translation.py`.
- [x] `core/config.py` created with `Settings` (BaseSettings) loading `OPENAI_API_KEY` from `.env`.
- [x] Scaffolded Vue 3 + Vite project in `frontend/` (JavaScript, no TS, blank project), installed npm deps.
- [x] Created `backend/.env.example` with `OPENAI_API_KEY=your_key_here`.
- [x] Created root `.gitignore` (covers `.env`, `node_modules`, `__pycache__`, `.venv`).
- [x] Created `README.md` with dev and Docker run instructions.

---

## 🔌 PHASE 2 — Backend API & AI Integration

**Goal:** Create a working `/translate` endpoint that calls OpenAI API.

### Tasks

- [x] Define Pydantic models:
  - `TranslationRequest(text: str, mode: str = "simple")`
  - `TranslationResponse(translated_text: str)`
- [ ] Create `call_ai(prompt: str) -> str` function using OpenAI SDK
- [ ] Implement `POST /translate` endpoint:
  - Build different system prompts based on `mode`:
    - `simple`: "Explain this in simple terms: {text}"
    - `eli5`: "Explain like I'm 10 years old: {text}"
    - `professional`: "Translate to professional non-technical language: {text}"
    - `analogies`: "Use an analogy to explain: {text}"
  - Call `call_ai()` and return JSON
- [ ] Add CORS middleware (allow `http://localhost:5173`)
- [ ] Add basic error handling (missing API key, timeout, malformed response)

### ✅ Progress

- [ ]

---

## 🎨 PHASE 3 — Frontend UI

**Goal:** Build a functional Vue interface that communicates with the backend.

### Tasks

- [ ] In `frontend/src/App.vue`, create:
  - Textarea for user input (v-model)
  - Select dropdown for mode (simple, eli5, professional, analogies)
  - Translate button
  - Div to display the translated result
- [ ] Add loading state ("Translating...") while fetching
- [ ] Add error message display (if backend fails)
- [ ] Use `fetch` to call `http://localhost:8000/translate` with `POST` and JSON body
- [ ] Style minimally (basic CSS or Tailwind – not critical)

### ✅ Progress

- [ ]

---

## 🧠 PHASE 4 — Multi-Mode Polish

**Goal:** Refactor prompt logic and ensure all four modes work well.

### Tasks

- [ ] Refactor backend prompt builder into a separate function `build_prompt(text, mode)`
- [ ] Test each mode with sample inputs (e.g., "What is a microservice?")
- [ ] Fine-tune system prompts for better output quality
- [ ] Add a small note in frontend about which mode is active

### ✅ Progress

- [ ]

---

## 🐳 PHASE 5 — Dockerization

**Goal:** Containerize both backend and frontend so the app runs with `docker-compose up`.

### Tasks

- [ ] Create `backend/Dockerfile`:
  - Use `python:3.11-slim`
  - Copy `requirements.txt`, install deps
  - Copy source code
  - Expose port 8000
  - Run `uvicorn main:app --host 0.0.0.0 --port 8000`
- [ ] Create `frontend/Dockerfile`:
  - Use `node:18-alpine` as build stage
  - Run `npm run build`
  - Use `nginx:alpine` to serve the `dist` folder
  - Expose port 80
- [ ] Create `docker-compose.yml`:
  - Backend service (build `./backend`, ports `8000:8000`, env file)
  - Frontend service (build `./frontend`, ports `8080:80`)
- [ ] Update `README.md` with Docker instructions:

  ```bash
  cp backend/.env.example backend/.env
  # Add your OpenAI API key to backend/.env
  docker-compose up
  ```

  - Test that the app works at `http://localhost:8080`

### ✅ Progress

- [ ]
