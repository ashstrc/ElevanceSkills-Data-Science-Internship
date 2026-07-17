class ResponseValidator:

    def __init__(self, engine):
        self.engine = engine

    # -------------------------------------------------------------

    def validate(self, evidence, question, answer):

        prompt = f"""
You are an AI response validator.

Your job is to evaluate whether the MAIN CONCLUSION of an answer is supported by the visual evidence.

Do NOT reject an answer because of minor wording differences or harmless elaboration.

==================================================
VISUAL EVIDENCE
==================================================

{evidence}

==================================================
QUESTION
==================================================

{question}

==================================================
ANSWER
==================================================

{answer}

==================================================
VALIDATION RULES
==================================================

SUPPORTED

Return SUPPORTED if the main conclusion agrees with the evidence.

Minor wording differences are acceptable.

Examples:

Evidence:
Activities: Resting

Answer:
"The tiger is resting peacefully."

→ SUPPORTED

--------------------------------------------

PARTIALLY SUPPORTED

Return PARTIALLY SUPPORTED if the answer is mostly correct but contains small assumptions that are not directly visible.

Example:

Evidence:
Tiger

Answer:
"The tiger appears calm and relaxed."

→ PARTIALLY SUPPORTED

--------------------------------------------

UNSUPPORTED

Return UNSUPPORTED ONLY if the answer contradicts the evidence or introduces important unsupported facts.

Examples:

Evidence:
Tiger

Answer:
"The tiger is five years old."

→ UNSUPPORTED

Evidence:
Tiger resting

Answer:
"The tiger is flying."

→ UNSUPPORTED

==================================================

Return EXACTLY this format:

STATUS: SUPPORTED / PARTIALLY SUPPORTED / UNSUPPORTED

CONFIDENCE: HIGH / MEDIUM / LOW

REASON: One sentence.
"""

        response = self.engine.generate(prompt)

        status = "UNKNOWN"
        confidence = "UNKNOWN"
        reason = response

        for line in response.splitlines():

            if line.startswith("STATUS:"):
                status = line.replace("STATUS:", "").strip()

            elif line.startswith("CONFIDENCE:"):
                confidence = line.replace("CONFIDENCE:", "").strip()

            elif line.startswith("REASON:"):
                reason = line.replace("REASON:", "").strip()

        return {
            "status": status,
            "confidence": confidence,
            "reason": reason
        }