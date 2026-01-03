"""
Tokenizer module for counting tokens and loading linguistic models.
"""
import tiktoken
import spacy
from typing import Any


class Tokenizer:
    def __init__(self, model_name: str = "en_core_web_sm"):
        self.encoding = tiktoken.get_encoding("cl100k_base")
        self._nlp = None
        self._model_name = model_name

    @property
    def nlp(self) -> Any:
        """Lazy-load Spacy model on first access."""
        if self._nlp is None:
            try:
                self._nlp = spacy.load(self._model_name)
            except OSError:
                print(f"Downloading Spacy model '{self._model_name}'...")
                from spacy.cli import download

                download(self._model_name)
                self._nlp = spacy.load(self._model_name)
        return self._nlp

    def count_tokens(self, text: str) -> int:
        return len(self.encoding.encode(text))

    def get_spacy_doc(self, text: str) -> Any:
        return self.nlp(text)
