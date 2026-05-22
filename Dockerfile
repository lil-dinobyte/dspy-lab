# syntax=docker/dockerfile:1
FROM python:3.12-slim-bookworm

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

ENV UV_PROJECT_ENVIRONMENT=/opt/venv \
    UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy

WORKDIR /workspace

COPY pyproject.toml uv.lock ./

RUN --mount=type=cache,target=/root/.cache/uv \
    uv sync --frozen

ENV PATH="/opt/venv/bin:$PATH"
ENV PYTHONPATH=/workspace/src

# Sin volumen: arranca Jupyter. Con compose se sincroniza de nuevo tras montar el repo.
CMD ["sh", "-c", "cd /workspace && uv sync --frozen && exec uv run --frozen jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root"]
