class ConversationMemory:

    MAX_HISTORY = 6

    def __init__(self):

        self.history = []

    def _trim_history(self):

        if len(self.history) > self.MAX_HISTORY:

            self.history = self.history[-self.MAX_HISTORY:]

    def add_user_message(self, message):

        self.history.append({

            "role": "user",

            "content": message

        })

        self._trim_history()

    def add_assistant_message(self, message):

        self.history.append({

            "role": "assistant",

            "content": message

        })

        self._trim_history()

    def get_history(self):

        return self.history

    def get_chat_messages(self):

        messages = [

            {

                "role": "system",

                "content": (
                    "You are an AI Research Assistant. "
                    "Answer questions using the previous conversation "
                    "and explain research papers in simple language."
                )

            }

        ]

        messages.extend(self.history)

        return messages

    def clear(self):

        self.history.clear()


if __name__ == "__main__":

    memory = ConversationMemory()

    memory.add_user_message(
        "What is Reinforcement Learning?"
    )

    memory.add_assistant_message(
        "Reinforcement Learning is a machine learning technique where an agent learns through rewards and penalties."
    )

    memory.add_user_message(
        "How is it different from supervised learning?"
    )

    memory.add_assistant_message(
        "Supervised learning uses labeled data, while Reinforcement Learning learns through rewards and interactions."
    )

    print("\nConversation History:\n")

    for message in memory.get_history():

        print(f"{message['role'].upper()}: {message['content']}")

    print("\n" + "=" * 60)

    print("\nMessages Passed to SmolLM2:\n")

    for message in memory.get_chat_messages():

        print(f"{message['role'].upper()}:")

        print(message["content"])

        print()