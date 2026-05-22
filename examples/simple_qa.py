from __future__ import annotations

import dspy

from dspy_lab.lm_config import configure_lm


def main() -> None:
    configure_lm(max_tokens=512)
    qa = dspy.Predict("pregunta: str -> respuesta: str")
    pred = qa(pregunta="Que es DSPy en una frase?")
    print(pred.respuesta)


if __name__ == "__main__":
    main()
