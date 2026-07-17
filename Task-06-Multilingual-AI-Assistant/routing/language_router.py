"""
language_router.py
------------------

Multilingual routing layer.

Responsibilities
----------------
• Preprocess multilingual user input.
• Normalize text into the assistant's canonical language.
• Pass normalized text into the reasoning pipeline.
• Localize assistant responses.
• Preserve multilingual conversation context.

This module acts as a bridge between the
Language Processor and the existing
Task-05 reasoning engine.

Author:
Ashmit Kumar
"""

from __future__ import annotations

from typing import Callable, Optional

from language.processor import LanguageProcessor
from memory.multilingual_memory import MultilingualMemory


class LanguageRouter:
    """
    Routes multilingual conversations through the
    existing reasoning engine.

    The reasoning engine remains completely
    language-agnostic.
    """

    def __init__(
        self,
        reasoning_engine: Callable[[str], str],
        memory: Optional[MultilingualMemory] = None,
    ):

        self.language_processor = LanguageProcessor()

        self.reasoning_engine = reasoning_engine

        self.memory = (
            memory
            if memory is not None
            else MultilingualMemory()
        )

    # -------------------------------------------------------------

    def process(self, user_input: str) -> str:
        """
        Complete multilingual processing pipeline.

        Flow

        User
          ↓
        Detect Language
          ↓
        Translate (if required)
          ↓
        Existing Reasoning Engine
          ↓
        Translate Back
          ↓
        Save Memory
          ↓
        Final Response
        """

        # Process user input
        context = self.language_processor.process_input(
            user_input
        )

        # Existing reasoning engine
        assistant_response = self.reasoning_engine(
            context.normalized_text
        )

        # Translate response back
        localized_response = (
            self.language_processor.process_output(
                assistant_response,
                context,
            )
        )

        # Store conversation
        self.memory.add_turn(
            context=context,
            assistant_response=localized_response,
        )

        return localized_response

    # -------------------------------------------------------------

    def history(self):
        """
        Return multilingual conversation history.
        """

        return self.memory.get_history()

    # -------------------------------------------------------------

    def canonical_history(self):
        """
        Returns canonical conversation history.

        Useful for prompts.
        """

        return self.memory.get_canonical_history()

    # -------------------------------------------------------------

    def clear(self):
        """
        Clear multilingual conversation.
        """

        self.memory.clear()

    # -------------------------------------------------------------

    def last_language(self):
        """
        Returns last detected language.
        """

        return self.memory.last_language()

    # -------------------------------------------------------------

    def supported_languages(self):
        """
        Supported languages.
        """

        return (
            self.language_processor
            .supported_languages()
        )

    # -------------------------------------------------------------

    def detect_language(
        self,
        text: str,
    ):
        """
        Detect language only.
        """

        return (
            self.language_processor
            .detect_language(text)
        )