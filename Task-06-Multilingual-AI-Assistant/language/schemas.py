from dataclasses import dataclass
from typing import Optional


@dataclass
class LanguageContext:
    original_text: str
    normalized_text: str

    primary_language: str
    secondary_language: Optional[str] = None

    confidence: float = 0.0

    is_mixed: bool = False
    translation_required: bool = False