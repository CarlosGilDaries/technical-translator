# AI Technical Translator

Una aplicación web que traduce texto técnico o complejo a un lenguaje claro y fácil de entender. Soporta cuatro modos de explicación: **simple**, **ELI5**, **profesional no técnico** y **basado en analogías**.

## Tecnologías

- **Backend:** FastAPI, Uvicorn, Groq API (Llama 3.3 70B), Pydantic, python-dotenv
- **Frontend:** Vue 3 + Vite, Fetch API, Bootstrap

## Obtener una API Key de Groq

1. Ve a [https://console.groq.com/keys](https://console.groq.com/keys)
2. Inicia sesión o crea una cuenta gratuita
3. Haz clic en **Create API Key**, ponle un nombre y guárdala (Groq no volverá a mostrártela, por lo que es conveniente pegarla en un lugar seguro antes de continuar)

## Ejecución sin Docker (Desarrollo)

```bash
git clone https://github.com/CarlosGilDaries/technical-translator.git
```

### Backend (terminal 1)

```bash
cd technical-translator
cd backend
python -m venv .venv

# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate

pip install -r requirements.txt
cp .env.example .env
# Edita .env y añade tu API key de Groq
uvicorn main:app --reload --port 8000
```

### Frontend (terminal 2)

```bash
cd technical-translator
cd frontend
npm install
npm run dev
```

El frontend estará disponible en http://localhost:5173 y la API del backend en http://localhost:8000.

### Health check

```
http://localhost:8000/health
```

### Documentación de la API (Swagger UI)

FastAPI genera documentación interactiva automáticamente:

```
http://localhost:8000/docs
```

## Ejecución con Docker

```bash
git clone https://github.com/CarlosGilDaries/technical-translator.git
cd technical-translator
cp backend/.env.example backend/.env
# Añade tu API key de Groq en backend/.env
docker-compose up
```

La aplicación estará disponible en http://localhost:8080.
