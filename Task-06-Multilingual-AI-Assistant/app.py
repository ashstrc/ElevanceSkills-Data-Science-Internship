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

from language.processor import LanguageProcessor

# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Multilingual AI Assistant",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Multilingual AI Assistant")
st.caption("Task-06 • Multilingual Multimodal AI Assistant")

# ============================================================
# SESSION STATE
# ============================================================

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

if "language" not in st.session_state:
    st.session_state.language = LanguageProcessor()

# ============================================================
# MODEL LOADING
# ============================================================

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

# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Assistant Mode")

mode = st.sidebar.radio(

    "Choose Mode",

    [

        "💬 Text Chat",

        "🖼 Image Analysis",

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

st.sidebar.markdown("---")

st.sidebar.subheader("Language")

st.sidebar.info(
    st.session_state.memory.get_language()
)

# ============================================================
# TEXT CHAT
# ============================================================

if mode == "💬 Text Chat":

    st.header("💬 Text Chat")

    user_input = st.text_area(

        "Ask anything",

        height=140

    )

    if st.button("Ask"):

        if not user_input.strip():

            st.warning("Please enter a question.")

        else:

            engine = load_reasoner()

            language_processor = st.session_state.language

            with st.spinner("Detecting language..."):

                context = language_processor.process_input(
                    user_input
                )

            st.info(
                f"Detected Language : {context.primary_language.upper()} "
                f"(Confidence: {context.confidence:.2f})"
            )

            with st.spinner("Thinking..."):

                response = engine.generate(
                    context.normalized_text
                )

            final_response = language_processor.process_output(
                response,
                context
            )

            st.session_state.memory.add_interaction(

                question=context.original_text,

                normalized_question=context.normalized_text,

                answer=final_response,

                language=context.primary_language

            )

            st.success("Assistant")

            st.write(final_response)

            with st.expander("Conversation History"):

                st.text(
                    st.session_state.memory.get_history()
                )
                
                
                # ============================================================
# IMAGE ANALYSIS
# ============================================================

elif mode == "🖼 Image Analysis":

    st.header("🖼 Image Analysis")

    uploaded_file = st.file_uploader(
        "Upload an image",
        type=["jpg", "jpeg", "png", "webp"],
        key="image_analysis"
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

            try:

                with st.spinner("Extracting visual evidence..."):

                    evidence = vision.extract_visual_evidence(
                        temp_path
                    )

                st.session_state.memory.set_image(
                    temp_path
                )

                st.session_state.memory.set_evidence(
                    evidence
                )

                scene = (
                    st.session_state.scene_builder.build_scene(
                        evidence
                    )
                )

                st.session_state.scene = scene

                st.success("Visual Evidence")

                st.code(
                    evidence,
                    language="text"
                )

                st.subheader("Structured Scene")

                st.json(scene)

            finally:

                if os.path.exists(temp_path):

                    os.remove(temp_path)
                    
                    
                    # ============================================================
# IMAGE + QUESTION
# ============================================================

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

            try:

                with st.spinner("Extracting visual evidence..."):

                    evidence = vision.extract_visual_evidence(
                        temp_path
                    )

                scene = (
                    st.session_state.scene_builder.build_scene(
                        evidence
                    )
                )

                st.session_state.evidence = evidence

                st.session_state.scene = scene

                st.session_state.memory.set_image(
                    temp_path
                )

                st.session_state.memory.set_evidence(
                    evidence
                )

                st.success("Visual Evidence Extracted")

            finally:

                if os.path.exists(temp_path):

                    os.remove(temp_path)

        if st.session_state.evidence is not None:

            st.subheader("Visual Evidence")

            st.code(
                st.session_state.evidence,
                language="text"
            )

            user_question = st.text_input(
                "Ask a question about this image"
            )

            if st.button("Ask Question"):

                if not user_question.strip():

                    st.warning("Please enter a question.")

                else:

                    language_processor = st.session_state.language

                    context = language_processor.process_input(
                        user_question
                    )

                    route = st.session_state.router.route(
                        context.normalized_text
                    )

                    engine = load_reasoner()
                    
                    
                                        # =====================================================
                    # DIRECT EVIDENCE
                    # =====================================================

                    if route == QuestionRouter.DIRECT_EVIDENCE:

                        answer = st.session_state.answerer.answer(
                            context.normalized_text,
                            st.session_state.scene
                        )

                        if answer is None:

                            answer = (
                                "The requested information could not be "
                                "found in the extracted visual evidence."
                            )

                    # =====================================================
                    # VISUAL REASONING
                    # =====================================================

                    elif route == QuestionRouter.VISUAL_REASONING:

                        history = (
                            st.session_state.memory.get_history()
                        )

                        prompt = (
                            st.session_state.reasoner.build_prompt(
                                evidence=st.session_state.evidence,
                                question=context.normalized_text,
                                history=history
                            )
                        )

                        with st.spinner("Reasoning..."):

                            answer = engine.generate(prompt)

                    # =====================================================
                    # MEMORY REASONING
                    # =====================================================

                    elif route == QuestionRouter.MEMORY_REASONING:

                        history = (
                            st.session_state.memory.get_history()
                        )

                        prompt = (
                            st.session_state.reasoner.build_prompt(
                                evidence=st.session_state.evidence,
                                question=context.normalized_text,
                                history=history
                            )
                        )

                        with st.spinner("Reasoning using conversation memory..."):

                            answer = engine.generate(prompt)

                    # =====================================================
                    # IMAGE ANALYSIS
                    # =====================================================

                    elif route == QuestionRouter.IMAGE_ANALYSIS:

                        answer = st.session_state.evidence

                    # =====================================================
                    # DEFAULT TEXT
                    # =====================================================

                    else:

                        with st.spinner("Generating response..."):

                            answer = engine.generate(
                                context.normalized_text
                            )

                    final_answer = (
                        language_processor.process_output(
                            answer,
                            context
                        )
                    )
                    
                    
                                        # =====================================================
                    # RESPONSE VALIDATION
                    # =====================================================

                    if route != QuestionRouter.IMAGE_ANALYSIS:

                        validation = (
                            st.session_state.validator.validate(
                                evidence=st.session_state.evidence,
                                question=context.normalized_text,
                                answer=final_answer
                            )
                        )

                    else:

                        validation = {
                            "status": "NOT APPLICABLE",
                            "confidence": "-",
                            "reason": "Visual evidence displayed directly."
                        }

                    # =====================================================
                    # MEMORY UPDATE
                    # =====================================================

                    st.session_state.memory.add_interaction(

                        question=context.original_text,

                        normalized_question=context.normalized_text,

                        answer=final_answer,

                        language=context.primary_language

                    )

                    # =====================================================
                    # DISPLAY RESPONSE
                    # =====================================================

                    st.subheader("Assistant Response")

                    st.write(final_answer)

                    st.markdown("---")

                    col1, col2 = st.columns(2)

                    with col1:

                        st.metric(
                            "Detected Language",
                            context.primary_language.upper()
                        )

                    with col2:

                        st.metric(
                            "Confidence",
                            f"{context.confidence:.2%}"
                        )

                    st.markdown("---")

                    st.subheader("Validation Report")

                    st.json(validation)

                    with st.expander("Conversation History"):

                        st.text(
                            st.session_state.memory.get_history()
                        )

# ============================================================
# END OF APPLICATION
# ============================================================