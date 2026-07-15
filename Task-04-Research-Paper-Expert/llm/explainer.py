from transformers import AutoTokenizer
from transformers import AutoModelForCausalLM
import torch

from memory.conversation import ConversationMemory


MODEL_NAME = "HuggingFaceTB/SmolLM2-1.7B-Instruct"


class ResearchExplainer:

    def __init__(self):

        print("Loading SmolLM2 Model...")

        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_NAME
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float32,
            device_map="cpu"
        )

        self.memory = ConversationMemory()

        print("SmolLM2 Ready!")

    def explain(self, question, summary):

        self.memory.add_user_message(
            f"""
Question:
{question}

Research Summary:
{summary}

Explain this paper in simple English.

Your answer should include:

1. What is the concept?
2. Why is it important?
3. How does it work?
4. One practical example.

Keep the explanation under 180 words.
"""
        )

        messages = self.memory.get_chat_messages()

        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt"
        )

        attention_mask = torch.ones_like(inputs)

        outputs = self.model.generate(
            input_ids=inputs,
            attention_mask=attention_mask,
            max_new_tokens=200,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            repetition_penalty=1.15,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id
        )

        generated_tokens = outputs[0][inputs.shape[-1]:]

        answer = self.tokenizer.decode(
            generated_tokens,
            skip_special_tokens=True
        ).strip()

        self.memory.add_assistant_message(answer)

        return answer

    def show_memory(self):

        print("\nConversation Memory:\n")

        for message in self.memory.get_history():

            print(f"{message['role'].upper()}:")

            print(message["content"])

            print("-" * 60)


if __name__ == "__main__":

    explainer = ResearchExplainer()

    while True:

        question = input("\nQuestion (type 'exit' to quit):\n")

        if question.lower() == "exit":
            break

        summary = input("\nSummary:\n")

        print("\nGenerating Explanation...\n")

        explanation = explainer.explain(
            question,
            summary
        )

        print("\nExplanation:\n")

        print(explanation)

        print("\n" + "=" * 80)

        explainer.show_memory()

        print("=" * 80)