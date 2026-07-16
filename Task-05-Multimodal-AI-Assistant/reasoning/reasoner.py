class Reasoner:

    def __init__(self):
        pass

    # -------------------------------------------------------

    def build_prompt(
        self,
        evidence,
        question,
        history=""
    ):

        prompt = f"""
You are an intelligent multimodal AI assistant.

Your job is to answer the user's question ONLY using the provided visual evidence and conversation history.

==============================
VISUAL EVIDENCE
==============================

{evidence}

==============================
CONVERSATION HISTORY
==============================

{history}

==============================
CURRENT QUESTION
==============================

{question}

==============================
INSTRUCTIONS
==============================

1. Use ONLY the visual evidence.
2. If the evidence clearly identifies something, trust it.
3. Never contradict the evidence.
4. If information is missing, clearly state that the evidence is insufficient.
5. Use conversation history whenever it is relevant.
6. Never invent facts.
7. Explain your reasoning naturally.
8. Answer in a clear and concise way.

Answer:
"""

        return prompt