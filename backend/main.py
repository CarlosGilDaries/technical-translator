from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="AI Technical Translator Pro",
    description="Translates technical text into easy-to-understand language.",
    version="0.1.0",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check() -> dict:
    """Return the health status of the API.

    Returns:
        dict: A dictionary with key 'status' set to 'ok'.
    """
    return {"status": "ok"}
