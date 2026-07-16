import streamlit as st
from PIL import Image
import tempfile
import os

from vision.image_analyzer import ImageAnalyzer
from vision.scene_builder import SceneBuilder

from reasoning.reasoner import Reasoner
from llm.explainer import ReasoningEngine

from routing.question_router import QuestionRouter
from answering.evidence_answerer import EvidenceAnswerer

from validation.validator import ResponseValidator
from memory.conversation import ConversationMemory

st.set_page_config(
    page_title="Multimodal AI Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multimodal AI Assistant")
st.caption("Task-05 • Image + Text Reasoning Assistant")

if "vision" not in st.session_state:
    st.session_state.vision = None

if "engine" not in st.session_state:
    st.session_state.engine = None

if "validator" not in st.session_state:
    st.session_state.validator = None

if "memory" not in st.session_state:
    st.session_state.memory = ConversationMemory()

if "scene_builder" not in st.session_state:
    st.session_state.scene_builder = SceneBuilder()

if "router" not in st.session_state:
    st.session_state.router = QuestionRouter()

if "answerer" not in st.session_state:
    st.session_state.answerer = EvidenceAnswerer()

if "reasoner" not in st.session_state:
    st.session_state.reasoner = Reasoner()
    
def load_vision():

    if st.session_state.vision is None:

        with st.spinner("Loading Qwen2.5-VL..."):

            st.session_state.vision = ImageAnalyzer()

    return st.session_state.vision


def load_reasoner():

    if st.session_state.engine is None:

        with st.spinner("Loading SmolLM2..."):

            st.session_state.engine = ReasoningEngine()

            st.session_state.validator = ResponseValidator(
                st.session_state.engine
            )

    return st.session_state.engine

st.sidebar.title("Assistant Mode")

mode = st.sidebar.radio(

    "Choose a mode",

    [

        "💬 Text Chat",

        "🖼️ Image Analysis",

        "🧠 Image + Question"

    ]

)

st.sidebar.markdown("---")
st.sidebar.subheader("Loaded Models")

if st.session_state.engine:

    st.sidebar.success("✅ SmolLM2")

else:

    st.sidebar.info("SmolLM2 not loaded")

if st.session_state.vision:

    st.sidebar.success("✅ Qwen2.5-VL")

else:

    st.sidebar.info("Qwen2.5-VL not loaded")
    
# =====================================================
# TEXT CHAT
# =====================================================

if mode == "💬 Text Chat":

    st.header("💬 Text Chat")

    question = st.text_area(
        "Ask anything",
        height=120
    )

    if st.button("Ask"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            engine = load_reasoner()

            with st.spinner("Thinking..."):

                answer = engine.generate(question)

            st.success("Answer")

            st.write(answer)
            
            
# =====================================================
# IMAGE ANALYSIS
# =====================================================

elif mode == "🖼️ Image Analysis":

    st.header("🖼️ Image Analysis")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png", "webp"]
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if st.button("Analyze Image"):

            vision = load_vision()

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            ) as tmp:

                image.save(tmp.name)

                temp_path = tmp.name

            with st.spinner("Extracting visual evidence..."):

                evidence = vision.extract_visual_evidence(temp_path)

            os.remove(temp_path)

            st.success("Visual Evidence")

            st.code(
                evidence,
                language="text"
            )
            
# =====================================================
# IMAGE + QUESTION
# =====================================================

elif mode == "🧠 Image + Question":

    st.header("🧠 Image + Question")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png", "webp"],
        key="image_question"
    )

    if uploaded_file is not None:

        image = Image.open(uploaded_file)

        st.image(
            image,
            caption="Uploaded Image",
            use_container_width=True
        )

        if "evidence" not in st.session_state:
            st.session_state.evidence = None

        if "scene" not in st.session_state:
            st.session_state.scene = None

        if st.button("Extract Visual Evidence"):

            vision = load_vision()

            with tempfile.NamedTemporaryFile(
                delete=False,
                suffix=".jpg"
            ) as tmp:

                image.save(tmp.name)

                temp_path = tmp.name

            with st.spinner("Extracting visual evidence..."):

                evidence = vision.extract_visual_evidence(temp_path)

            os.remove(temp_path)

            st.session_state.evidence = evidence

            st.session_state.scene = (
                st.session_state.scene_builder.build_scene(evidence)
            )

        if st.session_state.evidence is not None:

            st.subheader("Visual Evidence")

            st.code(
                st.session_state.evidence,
                language="text"
            )

            question = st.text_input(
                "Ask a question about the image"
            )

            if st.button("Ask Question"):

                if question.strip() == "":

                    st.warning("Please enter a question.")

                else:
                    route = st.session_state.router.route(question)

                    engine = load_reasoner()

                    # ==========================================
                    # DIRECT EVIDENCE
                    # ==========================================

                    if route == QuestionRouter.DIRECT_EVIDENCE:

                        answer = st.session_state.answerer.answer(
                            question,
                            st.session_state.evidence
                        )

                    # ==========================================
                    # VISUAL REASONING
                    # ==========================================

                    elif route == QuestionRouter.VISUAL_REASONING:

                        prompt = st.session_state.reasoner.build_prompt(
                            question,
                            st.session_state.evidence,
                            st.session_state.scene
                        )

                        answer = engine.generate(prompt)

                    # ==========================================
                    # MEMORY REASONING
                    # ==========================================

                    elif route == QuestionRouter.MEMORY_REASONING:

                        prompt = st.session_state.reasoner.build_memory_prompt(
                            question,
                            st.session_state.memory
                        )

                        answer = engine.generate(prompt)

                    # ==========================================
                    # IMAGE ANALYSIS
                    # ==========================================

                    elif route == QuestionRouter.IMAGE_ANALYSIS:

                        answer = st.session_state.evidence

                    # ==========================================
                    # DEFAULT
                    # ==========================================

                    else:

                        answer = engine.generate(question)

                    validation = st.session_state.validator.validate(
                        answer,
                        st.session_state.evidence
                    )

                    st.session_state.memory.add_turn(
                        question,
                        answer
                    )

                    st.subheader("Answer")

                    st.write(answer)

                    st.subheader("Validation")

                    st.json(validation)