import re


class QuestionRouter:
    """
    Determines how a user question should be answered.

    Possible intents:

    - TEXT_CHAT
    - IMAGE_ANALYSIS
    - DIRECT_EVIDENCE
    - VISUAL_REASONING
    - MEMORY_REASONING
    """

    TEXT_CHAT = "TEXT_CHAT"
    IMAGE_ANALYSIS = "IMAGE_ANALYSIS"
    DIRECT_EVIDENCE = "DIRECT_EVIDENCE"
    VISUAL_REASONING = "VISUAL_REASONING"
    MEMORY_REASONING = "MEMORY_REASONING"

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def route(self, question: str):

        q = question.lower().strip()

        q = re.sub(r"[^\w\s]", "", q)

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
            r"describe the image"

        ]

        # =====================================================
        # MEMORY REASONING
        # =====================================================

        memory_patterns = [

            r"compare",
            r"previous image",
            r"last image",
            r"earlier image",
            r"before",
            r"difference",
            r"similar"

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

            r"effect"

        ]

        # =====================================================
        # DIRECT EVIDENCE
        # =====================================================

        evidence_patterns = [

            r"what animal",

            r"which animal",

            r"identify animal",

            r"identify the animal",

            r"what object",

            r"which object",

            r"what objects",

            r"how many",

            r"what color",

            r"which color",

            r"colour",

            r"what activity",

            r"what is it doing",

            r"what is he doing",

            r"what is she doing",

            r"activity",

            r"person",

            r"people",

            r"environment",

            r"background",

            r"text",

            r"visible text",

            r"what text",

            r"who is in",

            r"is there",

            r"does the image contain",

            r"animal",

            r"object"

        ]

        # =====================================================
        # CHECK MEMORY
        # =====================================================

        for pattern in memory_patterns:

            if re.search(pattern, q):

                return self.MEMORY_REASONING

        # =====================================================
        # CHECK IMAGE ANALYSIS
        # =====================================================

        for pattern in image_analysis_patterns:

            if re.search(pattern, q):

                return self.IMAGE_ANALYSIS

        # =====================================================
        # CHECK VISUAL REASONING
        # =====================================================

        for pattern in reasoning_patterns:

            if re.search(pattern, q):

                return self.VISUAL_REASONING

        # =====================================================
        # CHECK DIRECT EVIDENCE
        # =====================================================

        for pattern in evidence_patterns:

            if re.search(pattern, q):

                return self.DIRECT_EVIDENCE

        # =====================================================
        # DEFAULT
        # =====================================================

        return self.TEXT_CHAT