# dspy-lab

Laboratorio minimo para probar DSPy con OpenAI u Ollama, usando notebooks,
FastAPI y Docker Compose.

## Estructura

```text
src/dspy_lab/        Codigo reusable del proyecto
src/dspy_lab/api/    API FastAPI
notebooks/          Experimentos interactivos
examples/           Scripts de ejemplo
tests/              Pruebas automaticas
```

## Configuracion

1. Copia `.env.example` a `.env`.
2. Ajusta el backend:
   - `DSPY_LM_BACKEND=openai` para OpenAI.
   - `DSPY_LM_BACKEND=ollama` para Ollama.
3. Si usas OpenAI, define `OPENAI_API_KEY`.

## Uso local

Instala dependencias:

```sh
uv sync
```

Ejecuta la API:

```sh
$env:PYTHONPATH="src"
uv run uvicorn dspy_lab.api.main:app --reload
```

Prueba salud:

```sh
curl http://localhost:8000/health
```

## Docker

API con Ollama:

```sh
docker compose up api ollama
```

Jupyter Lab:

```sh
docker compose up lab ollama
```

## Tests

```sh
$env:PYTHONPATH="src"
uv run python -m unittest discover -s tests
```
