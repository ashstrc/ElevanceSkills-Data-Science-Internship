class ModeSelector:
    """
    Handles the initial interaction with the user and
    determines which assistant mode should be used.
    """

    TEXT_CHAT = "TEXT_CHAT"
    IMAGE_ANALYSIS = "IMAGE_ANALYSIS"
    IMAGE_QUESTION = "IMAGE_QUESTION"

    def select_mode(self):

        print("=" * 60)
        print("        MULTIMODAL AI ASSISTANT")
        print("=" * 60)

        print("\nSelect Mode:\n")

        print("1. Text Chat")
        print("2. Image Analysis")
        print("3. Image + Question")

        while True:

            choice = input("\nEnter choice (1-3): ").strip()

            if choice == "1":
                return self.TEXT_CHAT

            elif choice == "2":
                return self.IMAGE_ANALYSIS

            elif choice == "3":
                return self.IMAGE_QUESTION

            print("\nInvalid choice. Please enter 1, 2 or 3.")