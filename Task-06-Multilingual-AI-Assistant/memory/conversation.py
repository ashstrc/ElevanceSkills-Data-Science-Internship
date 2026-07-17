"""
conversation.py
---------------

Multilingual conversation memory for Task-06.

Responsibilities
----------------
• Preserve image context.
• Preserve multilingual conversation history.
• Store canonical (English) conversation.
• Maintain language continuity.
• Remain fully backward compatible with Task-05.

Author:
Ashmit Kumar
"""

from __future__ import annotations

from typing import Dict, List, Optional


class ConversationMemory:

    def __init__(self):

        self.current_image: Optional[str] = None

        self.current_evidence: str = ""

        self.history: List[Dict] = []

        self.current_language: str = "en"

    # ---------------------------------------------------------

    def has_image(self) -> bool:

        return self.current_image is not None

    # ---------------------------------------------------------

    def is_same_image(self, image_path: str) -> bool:

        return self.current_image == image_path

    # ---------------------------------------------------------

    def set_image(self, image_path: str):

        self.current_image = image_path

    # ---------------------------------------------------------

    def get_image(self):

        return self.current_image

    # ---------------------------------------------------------

    def set_evidence(self, evidence: str):

        self.current_evidence = evidence

    # ---------------------------------------------------------

    def get_evidence(self):

        return self.current_evidence

    # ---------------------------------------------------------

    def set_language(self, language: str):

        self.current_language = language

    # ---------------------------------------------------------

    def get_language(self):

        return self.current_language

    # ---------------------------------------------------------

    def add_interaction(
        self,
        question: str,
        answer: str,
        normalized_question: Optional[str] = None,
        language: str = "en",
    ):

        self.current_language = language

        self.history.append(
            {
                "question": question,
                "normalized_question": normalized_question
                if normalized_question
                else question,
                "answer": answer,
                "language": language,
            }
        )

    # ---------------------------------------------------------

    def get_history(self):

        if len(self.history) == 0:

            return "No previous conversation."

        conversation = []

        for i, item in enumerate(self.history, start=1):

            conversation.append(
                f"Q{i}: {item['normalized_question']}"
            )

            conversation.append(
                f"A{i}: {item['answer']}"
            )

        return "\n".join(conversation)

    # ---------------------------------------------------------

    def get_raw_history(self):

        return self.history

    # ---------------------------------------------------------

    def last_question(self):

        if not self.history:

            return None

        return self.history[-1]["question"]

    # ---------------------------------------------------------

    def last_answer(self):

        if not self.history:

            return None

        return self.history[-1]["answer"]

    # ---------------------------------------------------------

    def conversation_length(self):

        return len(self.history)

    # ---------------------------------------------------------

    def export(self):

        return {
            "image": self.current_image,
            "language": self.current_language,
            "history": self.history,
        }

    # ---------------------------------------------------------

    def clear(self):

        self.current_image = None

        self.current_evidence = ""

        self.current_language = "en"

        self.history.clear()