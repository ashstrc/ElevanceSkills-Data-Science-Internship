"""
question_router.py
------------------

Task-06 Multilingual Question Router

Responsibilities
----------------
• Route user questions.
• Support multilingual conversations.
• Preserve Task-05 routing logic.
• Remain backward compatible.

Author:
Ashmit Kumar
"""

from __future__ import annotations

import re

try:
    from language.detector import LanguageDetector
except Exception:
    LanguageDetector = None


class QuestionRouter:

    """
    Determines how a user question should be answered.

    Possible routes

    TEXT_CHAT
    IMAGE_ANALYSIS
    DIRECT_EVIDENCE
    VISUAL_REASONING
    MEMORY_REASONING
    """

    TEXT_CHAT = "TEXT_CHAT"

    IMAGE_ANALYSIS = "IMAGE_ANALYSIS"

    DIRECT_EVIDENCE = "DIRECT_EVIDENCE"

    VISUAL_REASONING = "VISUAL_REASONING"

    MEMORY_REASONING = "MEMORY_REASONING"

    # ---------------------------------------------------------

    def __init__(self):

        self.detector = None

        if LanguageDetector is not None:

            try:
                self.detector = LanguageDetector()
            except Exception:
                self.detector = None

    # ---------------------------------------------------------

    def detect_language(self, question: str):

        if self.detector is None:

            return {
                "primary_language": "en",
                "confidence": 1.0
            }

        try:

            return self.detector.detect(question)

        except Exception:

            return {
                "primary_language": "en",
                "confidence": 1.0
            }

    # ---------------------------------------------------------

    def preprocess(self, question: str):

        language = self.detect_language(question)

        normalized = question.lower().strip()

        normalized = re.sub(
            r"[^\w\s]",
            "",
            normalized
        )

        return normalized, language

    # ---------------------------------------------------------

    def route(self, question: str):

        q, language = self.preprocess(question)

        # =====================================================
        # IMAGE ANALYSIS
        # =====================================================

        image_analysis_patterns = [

            r"describe",

            r"analyze image",

            r"analyse image",

            r"summarize image",

            r"summarise image",

            r"caption",

            r"what do you see",

            r"describe this image",

            r"describe the image",

            # Hindi

            r"वर्णन",

            r"चित्र",

            r"छवि",

            r"क्या दिखाई",

            # Spanish

            r"describir",

            r"imagen",

            r"que ves",

            # French

            r"décrire",

            r"image",

            r"que voyez"
        ]

        # =====================================================
        # MEMORY
        # =====================================================

        memory_patterns = [

            r"compare",

            r"previous image",

            r"last image",

            r"earlier image",

            r"before",

            r"difference",

            r"similar",

            # Hindi

            r"पिछली",

            r"पहले",

            r"तुलना",

            # Spanish

            r"compar",

            r"anterior",

            # French

            r"compar",

            r"précéd"
        ]

        # =====================================================
        # VISUAL REASONING
        # =====================================================

        reasoning_patterns = [

            r"why",

            r"how",

            r"explain",

            r"reason",

            r"suggest",

            r"infer",

            r"predict",

            r"likely",

            r"possible",

            r"could",

            r"would",

            r"might",

            r"danger",

            r"safe",

            r"behavior",

            r"behaviour",

            r"cause",

            r"effect",

            # Hindi

            r"क्यों",

            r"कैसे",

            r"समझाइ",

            r"कारण",

            # Spanish

            r"por qué",

            r"como",

            r"explica",

            # French

            r"pourquoi",

            r"comment",

            r"expliquer"
        ]
        
                # =====================================================
        # DIRECT EVIDENCE
        # =====================================================

        evidence_patterns = [

            # -----------------------------
            # Animals
            # -----------------------------

            r"what animal",

            r"which animal",

            r"identify animal",

            r"identify the animal",

            r"animal",

            r"species",

            r"creature",

            # Hindi

            r"जानवर",

            r"पशु",

            r"कौन सा जानवर",

            # Spanish

            r"animal",

            r"especie",

            # French

            r"animal",

            r"espèce",

            # -----------------------------
            # Objects
            # -----------------------------

            r"what object",

            r"which object",

            r"what objects",

            r"identify object",

            r"object",

            r"objects",

            r"thing",

            r"things",

            # Hindi

            r"वस्तु",

            r"ऑब्जेक्ट",

            r"चीज",

            # Spanish

            r"objeto",

            r"objetos",

            # French

            r"objet",

            r"objets",

            # -----------------------------
            # Count
            # -----------------------------

            r"how many",

            r"count",

            r"number of",

            # Hindi

            r"कितने",

            r"संख्या",

            # Spanish

            r"cuántos",

            r"cantidad",

            # French

            r"combien",

            r"nombre",

            # -----------------------------
            # Colors
            # -----------------------------

            r"what color",

            r"which color",

            r"colour",

            r"color",

            # Hindi

            r"रंग",

            # Spanish

            r"color",

            # French

            r"couleur",

            # -----------------------------
            # Activities
            # -----------------------------

            r"what activity",

            r"activity",

            r"activities",

            r"what is it doing",

            r"what is he doing",

            r"what is she doing",

            r"doing",

            r"action",

            # Hindi

            r"क्या कर",

            r"गतिविध",

            # Spanish

            r"actividad",

            r"haciendo",

            # French

            r"activité",

            r"fait",

            # -----------------------------
            # People
            # -----------------------------

            r"person",

            r"people",

            r"human",

            r"man",

            r"woman",

            r"boy",

            r"girl",

            r"who",

            # Hindi

            r"व्यक्ति",

            r"लोग",

            r"आदमी",

            r"महिला",

            # Spanish

            r"persona",

            r"personas",

            r"hombre",

            r"mujer",

            # French

            r"personne",

            r"homme",

            r"femme",

            # -----------------------------
            # Environment
            # -----------------------------

            r"environment",

            r"background",

            r"location",

            r"place",

            r"where",

            # Hindi

            r"स्थान",

            r"जगह",

            r"पर्यावरण",

            # Spanish

            r"lugar",

            r"ubicación",

            r"fondo",

            # French

            r"endroit",

            r"lieu",

            r"arrière",

            # -----------------------------
            # Visible Text
            # -----------------------------

            r"text",

            r"visible text",

            r"written",

            r"writing",

            r"words",

            # Hindi

            r"लिखा",

            r"पाठ",

            r"टेक्स्ट",

            # Spanish

            r"texto",

            r"escrito",

            # French

            r"texte",

            r"écrit"
        ]

        # =====================================================
        # MEMORY REASONING
        # =====================================================

        for pattern in memory_patterns:

            if re.search(pattern, q):

                return self.MEMORY_REASONING

        # =====================================================
        # IMAGE ANALYSIS
        # =====================================================

        for pattern in image_analysis_patterns:

            if re.search(pattern, q):

                return self.IMAGE_ANALYSIS
            
            
            
                    # =====================================================
        # VISUAL REASONING
        # =====================================================

        for pattern in reasoning_patterns:

            if re.search(pattern, q):

                return self.VISUAL_REASONING

        # =====================================================
        # DIRECT EVIDENCE
        # =====================================================

        for pattern in evidence_patterns:

            if re.search(pattern, q):

                return self.DIRECT_EVIDENCE

        # =====================================================
        # MULTILINGUAL FALLBACKS
        # =====================================================

        language_code = language.get("primary_language", "en")

        # If the language is not English and no rule matched,
        # default to reasoning instead of plain text chat.
        # This allows the LLM to answer multilingual questions.

        if language_code != "en":

            return self.VISUAL_REASONING

        # =====================================================
        # IMAGE QUESTION HEURISTICS
        # =====================================================

        # Short factual questions generally refer to
        # the current uploaded image.

        if len(q.split()) <= 8:

            image_keywords = [

                "this",
                "that",
                "image",
                "picture",
                "photo",
                "it",
                "its",

                # Hindi
                "यह",
                "इस",
                "उस",

                # Spanish
                "esta",
                "este",
                "eso",

                # French
                "cette",
                "cet",
                "cela",
            ]

            for keyword in image_keywords:

                if keyword in q:

                    return self.DIRECT_EVIDENCE

        # =====================================================
        # REASONING HEURISTICS
        # =====================================================

        reasoning_keywords = [

            "why",
            "how",
            "explain",
            "reason",
            "predict",
            "suggest",
            "infer",
            "because",
            "possible",

            # Hindi
            "क्यों",
            "कैसे",

            # Spanish
            "porque",
            "como",

            # French
            "pourquoi",
            "comment",
        ]

        for keyword in reasoning_keywords:

            if keyword in q:

                return self.VISUAL_REASONING

        # =====================================================
        # MEMORY HEURISTICS
        # =====================================================

        memory_keywords = [

            "previous",
            "last",
            "earlier",
            "before",
            "again",

            # Hindi
            "पहले",
            "पिछला",

            # Spanish
            "anterior",

            # French
            "précédent",
        ]

        for keyword in memory_keywords:

            if keyword in q:

                return self.MEMORY_REASONING

        # =====================================================
        # DEFAULT
        # =====================================================

        return self.TEXT_CHAT

    # ---------------------------------------------------------

    def get_language(self, question: str):

        """
        Returns detected language information.

        Example
        -------
        {
            "primary_language": "hi",
            "confidence": 0.98
        }
        """

        return self.detect_language(question)

    # ---------------------------------------------------------

    def supported_routes(self):

        return [

            self.TEXT_CHAT,

            self.IMAGE_ANALYSIS,

            self.DIRECT_EVIDENCE,

            self.VISUAL_REASONING,

            self.MEMORY_REASONING,

        ]