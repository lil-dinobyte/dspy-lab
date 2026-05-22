"""API minima de ejemplo para probar DSPy desde FastAPI."""

from __future__ import annotations

from contextlib import asynccontextmanager

import dspy
from fastapi import FastAPI
from pydantic import BaseModel, Field

from dspy_lab.lm_config import configure_lm


@asynccontextmanager
async def lifespan(_: FastAPI):
    configure_lm()
    yield


app = FastAPI(title="dspy-lab", lifespan=lifespan)

_qa = dspy.Predict("pregunta: str -> respuesta: str")


class AskIn(BaseModel):
    pregunta: str = Field(..., min_length=1, max_length=4000)


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/ask")
def ask(body: AskIn):
    pred = _qa(pregunta=body.pregunta)
    return {"respuesta": pred.respuesta}
