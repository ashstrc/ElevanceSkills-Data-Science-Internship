"""
translator.py
--------------

Production-ready multilingual translator using Meta's
NLLB-200 Distilled 600M model.

Responsibilities
----------------
• Translate between supported languages.
• Lazy-load model only once.
• CPU/GPU compatible.
• Thread-safe singleton loading.
• Automatic language validation.
• Clean API for the assistant.

Author:
Ashmit Kumar
"""

from __future__ import annotations

import threading
from typing import Dict

import torch
from transformers import (
    AutoTokenizer,
    AutoModelForSeq2SeqLM,
)


class Translator:
    """
    Multilingual translator powered by Meta NLLB-200.

    Example
    -------

    translator = Translator()

    english = translator.translate(
        text="नमस्ते",
        source_lang="hi",
        target_lang="en"
    )

    hindi = translator.translate(
        text="Hello",
        source_lang="en",
        target_lang="hi"
    )
    """

    MODEL_NAME = "facebook/nllb-200-distilled-600M"

    # Supported languages
    LANGUAGE_CODES: Dict[str, str] = {
        "en": "eng_Latn",
        "hi": "hin_Deva",
        "es": "spa_Latn",
        "fr": "fra_Latn",
        "de": "deu_Latn",
        "ja": "jpn_Jpan",
    }

    _lock = threading.Lock()
    _model = None
    _tokenizer = None

    def __init__(self):

        self.device = (
            "cuda"
            if torch.cuda.is_available()
            else "cpu"
        )

        self._load_model()

    @classmethod
    def _load_model(cls):
        """
        Loads tokenizer and model only once.
        """

        if cls._model is not None:
            return

        with cls._lock:

            if cls._model is not None:
                return

            print("Loading NLLB-200 Translator...")

            cls._tokenizer = AutoTokenizer.from_pretrained(
                cls.MODEL_NAME
            )

            cls._model = (
                AutoModelForSeq2SeqLM
                .from_pretrained(cls.MODEL_NAME)
            )

    def _validate_language(self, language: str):

        if language not in self.LANGUAGE_CODES:
            raise ValueError(
                f"Unsupported language: {language}"
            )

    def translate(
        self,
        text: str,
        source_lang: str,
        target_lang: str,
        max_new_tokens: int = 512,
    ) -> str:
        """
        Translate text.

        Parameters
        ----------
        text : str

        source_lang : str
            ISO language code
            Example:
            en
            hi
            es

        target_lang : str

        Returns
        -------
        str
            Translated text.
        """

        if not text.strip():
            return text

        if source_lang == target_lang:
            return text

        self._validate_language(source_lang)
        self._validate_language(target_lang)

        tokenizer = self.__class__._tokenizer
        model = self.__class__._model

        tokenizer.src_lang = self.LANGUAGE_CODES[source_lang]

        inputs = tokenizer(
            text,
            return_tensors="pt",
            truncation=True,
        )

        inputs = {
            key: value.to(self.device)
            for key, value in inputs.items()
        }

        model = model.to(self.device)

        with torch.no_grad():

            generated_tokens = model.generate(

                **inputs,

                forced_bos_token_id=tokenizer.convert_tokens_to_ids(
                    self.LANGUAGE_CODES[target_lang]
                ),

                max_new_tokens=max_new_tokens,

                num_beams=4,

                length_penalty=1.0,

                early_stopping=True,
            )

        translated = tokenizer.batch_decode(
            generated_tokens,
            skip_special_tokens=True,
        )[0]

        return translated.strip()

    # ------------------------------------------------------------------

    def to_english(
        self,
        text: str,
        source_lang: str,
    ) -> str:
        """
        Convenience helper.
        """

        return self.translate(
            text=text,
            source_lang=source_lang,
            target_lang="en",
        )

    # ------------------------------------------------------------------

    def from_english(
        self,
        text: str,
        target_lang: str,
    ) -> str:
        """
        Convenience helper.
        """

        return self.translate(
            text=text,
            source_lang="en",
            target_lang=target_lang,
        )

    # ------------------------------------------------------------------

    @property
    def supported_languages(self):

        return list(self.LANGUAGE_CODES.keys())