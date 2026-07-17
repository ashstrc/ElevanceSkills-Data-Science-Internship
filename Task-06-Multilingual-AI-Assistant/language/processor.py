"""
processor.py
------------

Central multilingual processing pipeline.

Responsibilities
----------------
• Detect input language.
• Determine whether translation is required.
• Translate incoming text into the assistant's
  canonical language (English).
• Translate assistant responses back into the
  user's preferred language.
• Produce LanguageContext objects.

Author:
Ashmit Kumar
"""

from __future__ import annotations

from language.detector import LanguageDetector
from language.schemas import LanguageContext
from language.translator import Translator


class LanguageProcessor:
    """
    Central multilingual processing pipeline.

    The rest of the assistant never directly talks
    to the detector or translator.

    It only communicates with this class.
    """

    def __init__(self):

        self.detector = LanguageDetector()
        self.translator = Translator()

        self.canonical_language = "en"

    # ---------------------------------------------------------

    def process_input(
        self,
        text: str,
    ) -> LanguageContext:
        """
        Process incoming user message.

        Returns
        -------
        LanguageContext
        """

        detection = self.detector.detect(text)

        language = detection["primary_language"]

        confidence = detection["confidence"]

        translation_required = (
            language != self.canonical_language
        )

        if translation_required:

            normalized = self.translator.translate(
                text=text,
                source_lang=language,
                target_lang=self.canonical_language,
            )

        else:

            normalized = text

        return LanguageContext(

            original_text=text,

            normalized_text=normalized,

            primary_language=language,

            confidence=confidence,

            translation_required=translation_required,

            is_mixed=False,
        )

    # ---------------------------------------------------------

    def process_output(
        self,
        response: str,
        context: LanguageContext,
    ) -> str:
        """
        Convert assistant response back to the
        user's preferred language.
        """

        if not context.translation_required:
            return response

        translated = self.translator.translate(

            text=response,

            source_lang=self.canonical_language,

            target_lang=context.primary_language,

        )

        return translated

    # ---------------------------------------------------------

    def detect_language(
        self,
        text: str,
    ) -> dict:
        """
        Expose raw detector output.
        """

        return self.detector.detect(text)

    # ---------------------------------------------------------

    def supported_languages(self):
        """
        Return supported language codes.
        """

        return self.translator.supported_languages