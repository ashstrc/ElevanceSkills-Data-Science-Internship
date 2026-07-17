from assistant.mode_selector import ModeSelector

from vision.image_analyzer import ImageAnalyzer
from vision.scene_builder import SceneBuilder

from routing.question_router import QuestionRouter
from answering.evidence_answerer import EvidenceAnswerer

from reasoning.reasoner import Reasoner
from llm.explainer import ReasoningEngine

from validation.validator import ResponseValidator
from memory.conversation import ConversationMemory


class AssistantController:

    def __init__(self):

        self.mode_selector = ModeSelector()

        self.router = QuestionRouter()

        self.scene_builder = SceneBuilder()

        self.answerer = EvidenceAnswerer()

        self.prompt_builder = Reasoner()

        self.memory = ConversationMemory()

        self.vision = None
        self.engine = None
        self.validator = None

    # -------------------------------------------------------------

    def load_vision(self):

        if self.vision is None:

            self.vision = ImageAnalyzer()

    # -------------------------------------------------------------

    def load_reasoner(self):

        if self.engine is None:

            self.engine = ReasoningEngine()

            self.validator = ResponseValidator(self.engine)

    # -------------------------------------------------------------

    def run(self):

        mode = self.mode_selector.select_mode()

        if mode == ModeSelector.TEXT_CHAT:

            self.run_text_chat()

        elif mode == ModeSelector.IMAGE_ANALYSIS:

            self.run_image_analysis()

        elif mode == ModeSelector.IMAGE_QUESTION:

            self.run_image_question()

    # -------------------------------------------------------------

    def run_text_chat(self):

        self.load_reasoner()

        print("\nType 'exit' to quit.\n")

        while True:

            question = input("You : ").strip()

            if question.lower() == "exit":
                break

            answer = self.engine.generate(question)

            print("\nAssistant:\n")
            print(answer)
            print()

    # -------------------------------------------------------------

    def run_image_analysis(self):

        self.load_vision()

        image_path = input("\nImage Path : ").strip()

        evidence = self.vision.extract_visual_evidence(image_path)

        print("\n" + "=" * 60)
        print("VISUAL EVIDENCE")
        print("=" * 60)
        print(evidence)

    # -------------------------------------------------------------

    def run_image_question(self):

        self.load_vision()

        print("\nType 'exit' anytime to quit.\n")

        while True:

            image_path = input("Image Path : ").strip()

            if image_path.lower() == "exit":
                return

            evidence = self.vision.extract_visual_evidence(image_path)

            scene = self.scene_builder.build_scene(evidence)

            self.memory.set_image(image_path)
            self.memory.set_evidence(evidence)

            print("\n" + "=" * 60)
            print("VISUAL EVIDENCE")
            print("=" * 60)
            print(evidence)

            while True:

                question = input("\nQuestion ('new' for another image): ").strip()

                if question.lower() == "exit":
                    return

                if question.lower() == "new":
                    break

                route = self.router.route(question)

                # -------------------------------------------------
                # IMAGE ANALYSIS
                # -------------------------------------------------

                if route == QuestionRouter.IMAGE_ANALYSIS:

                    print("\n" + "=" * 60)
                    print("VISUAL EVIDENCE")
                    print("=" * 60)
                    print(evidence)

                    continue

                # -------------------------------------------------
                # DIRECT EVIDENCE
                # -------------------------------------------------

                if route == QuestionRouter.DIRECT_EVIDENCE:

                    answer = self.answerer.answer(question, scene)

                    if answer is not None:

                        print("\n" + "=" * 60)
                        print("FINAL ANSWER")
                        print("=" * 60)
                        print(answer)
                        print("=" * 60)

                        self.memory.add_interaction(question, answer)

                        continue

                # -------------------------------------------------
                # REASONING
                # -------------------------------------------------

                self.load_reasoner()

                history = self.memory.get_history()

                prompt = self.prompt_builder.build_prompt(
                    evidence=evidence,
                    question=question,
                    history=history
                )

                print("\nGenerating response...\n")

                answer = self.engine.generate(prompt)
                
                report = self.validator.validate(
                    evidence=evidence,
                    question=question,
                    answer=answer
                )

                print("\n" + "=" * 60)
                print("FINAL ANSWER")
                print("=" * 60)
                print(answer)

                print("\n" + "=" * 60)
                print("VALIDATION REPORT")
                print("=" * 60)
                print(f"Status      : {report['status']}")
                print(f"Confidence  : {report['confidence']}")
                print(f"Reason      : {report['reason']}")
                print("=" * 60)

                self.memory.add_interaction(
                    question,
                    answer
                )