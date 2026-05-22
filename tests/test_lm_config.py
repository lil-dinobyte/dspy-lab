from __future__ import annotations

import os
import unittest
from unittest.mock import patch

from dspy_lab.lm_config import _normalize_ollama_model, _ollama_model_name_for_litellm


class OllamaModelConfigTests(unittest.TestCase):
    def test_normalize_adds_ollama_chat_prefix(self) -> None:
        self.assertEqual(_normalize_ollama_model("llama3.2:latest"), "ollama_chat/llama3.2:latest")

    def test_normalize_converts_ollama_prefix(self) -> None:
        self.assertEqual(_normalize_ollama_model("ollama/llama3.2:latest"), "ollama_chat/llama3.2:latest")

    def test_model_name_adds_latest_tag(self) -> None:
        self.assertEqual(_ollama_model_name_for_litellm("llama3.2"), "llama3.2:latest")

    def test_model_name_uses_environment_default(self) -> None:
        with patch.dict(os.environ, {"OLLAMA_MODEL": "mistral"}, clear=False):
            self.assertEqual(_ollama_model_name_for_litellm(None), "mistral:latest")


if __name__ == "__main__":
    unittest.main()
