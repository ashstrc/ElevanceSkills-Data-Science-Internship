class ConversationMemory:

    def __init__(self):
        self.current_image = None
        self.current_evidence = ""
        self.history = []

    # ---------------------------------

    def has_image(self):
        return self.current_image is not None

    # ---------------------------------

    def is_same_image(self, image_path):
        return self.current_image == image_path

    # ---------------------------------

    def set_image(self, image_path):
        self.current_image = image_path

    # ---------------------------------

    def set_evidence(self, evidence):
        self.current_evidence = evidence

    # ---------------------------------

    def get_evidence(self):
        return self.current_evidence

    # ---------------------------------

    def add_interaction(self, question, answer):

        self.history.append(
            {
                "question": question,
                "answer": answer
            }
        )

    # ---------------------------------

    def get_history(self):

        if len(self.history) == 0:
            return "No previous conversation."

        text = ""

        for i, item in enumerate(self.history, start=1):

            text += (
                f"Q{i}: {item['question']}\n"
                f"A{i}: {item['answer']}\n\n"
            )

        return text.strip()

    # ---------------------------------

    def clear(self):

        self.current_image = None
        self.current_evidence = ""
        self.history = []