"""
multilingual_memory.py
----------------------

Language-independent conversation memory.

Responsibilities
----------------
• Preserve conversational context.
• Preserve semantic meaning across language switches.
• Track user language preferences.
• Maintain multilingual conversation history.
• Provide context to the reasoning engine.

Author:
Ashmit Kumar
"""

from __future__ import annotations

from dataclasses import dataclass, field
from typing import Dict, List, Optional

from language.schemas import LanguageContext


@dataclass
class MemoryEntry:
    """
    Represents one conversation turn.
    """

    user_message: str
    assistant_message: str

    normalized_user_message: str

    language: str

    metadata: Dict = field(default_factory=dict)


class MultilingualMemory:
    """
    Multilingual conversation memory.

    Stores canonical (English) messages internally
    while preserving the user's original language.
    """

    def __init__(self):

        self.history: List[MemoryEntry] = []

        self.current_language = "en"

        self.last_context: Optional[LanguageContext] = None

    # -------------------------------------------------------------

    def add_turn(
        self,
        context: LanguageContext,
        assistant_response: str,
        metadata: Optional[Dict] = None,
    ) -> None:

        if metadata is None:
            metadata = {}

        entry = MemoryEntry(

            user_message=context.original_text,

            assistant_message=assistant_response,

            normalized_user_message=context.normalized_text,

            language=context.primary_language,

            metadata=metadata,

        )

        self.history.append(entry)

        self.current_language = context.primary_language

        self.last_context = context

    # -------------------------------------------------------------

    def get_history(self) -> List[MemoryEntry]:

        return self.history

    # -------------------------------------------------------------

    def get_canonical_history(self) -> List[str]:
        """
        Returns conversation in canonical language.

        Useful for LLM prompts.
        """

        conversation = []

        for item in self.history:

            conversation.append(
                f"User: {item.normalized_user_message}"
            )

            conversation.append(
                f"Assistant: {item.assistant_message}"
            )

        return conversation

    # -------------------------------------------------------------

    def last_user_message(self) -> Optional[str]:

        if not self.history:
            return None

        return self.history[-1].normalized_user_message

    # -------------------------------------------------------------

    def last_response(self) -> Optional[str]:

        if not self.history:
            return None

        return self.history[-1].assistant_message

    # -------------------------------------------------------------

    def last_language(self) -> str:

        return self.current_language

    # -------------------------------------------------------------

    def conversation_size(self) -> int:

        return len(self.history)

    # -------------------------------------------------------------

    def clear(self) -> None:

        self.history.clear()

        self.current_language = "en"

        self.last_context = None

    # -------------------------------------------------------------

    def export(self) -> Dict:
        """
        Export memory.

        Useful for debugging or persistence.
        """

        return {
            "language": self.current_language,
            "turns": self.conversation_size(),
            "history": [
                {
                    "user": item.user_message,
                    "assistant": item.assistant_message,
                    "normalized": item.normalized_user_message,
                    "language": item.language,
                    "metadata": item.metadata,
                }
                for item in self.history
            ],
        }