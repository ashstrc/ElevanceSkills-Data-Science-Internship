import os

# --------------------------------------------------------
# Hugging Face Cache
# --------------------------------------------------------

os.environ["HF_HOME"] = r"D:\hf_cache"
os.environ["HF_HUB_CACHE"] = r"D:\hf_cache"

import torch
from transformers import AutoTokenizer, AutoModelForCausalLM


MODEL_PATH = (
    r"D:\hf_cache\models--HuggingFaceTB--SmolLM2-1.7B-Instruct"
    r"\snapshots\31b70e2e869a7173562077fd711b654946d38674"
)


class ReasoningEngine:

    def __init__(self):

        print("Loading SmolLM2 Reasoning Engine...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.tokenizer = AutoTokenizer.from_pretrained(
            MODEL_PATH,
            local_files_only=True
        )

        self.model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            torch_dtype=torch.float32,
            local_files_only=True
        )

        self.model.to(self.device)
        self.model.eval()

        print("SmolLM2 Ready!")

    def generate(self, prompt):

        messages = [
        {
            "role": "user",
            "content": prompt
        }
    ]

        inputs = self.tokenizer.apply_chat_template(
            messages,
            tokenize=True,
            add_generation_prompt=True,
            return_tensors="pt"
    )

    # Move every tensor to the correct device
        inputs = {k: v.to(self.device) for k, v in inputs.items()}

        with torch.no_grad():

            outputs = self.model.generate(
            **inputs,
            max_new_tokens=120,
            do_sample=True,
            temperature=0.4,
            top_p=0.9,
            repetition_penalty=1.15,
            pad_token_id=self.tokenizer.eos_token_id,
            eos_token_id=self.tokenizer.eos_token_id
        )

        # Remove prompt tokens
        generated_tokens = outputs[:, inputs["input_ids"].shape[1]:]

        answer = self.tokenizer.batch_decode(
        generated_tokens,
        skip_special_tokens=True
        )[0]

        return answer.strip()


if __name__ == "__main__":

    engine = ReasoningEngine()

    while True:

        prompt = input("\nPrompt (type 'exit' to quit): ")

        if prompt.lower() == "exit":
            break

        print("\nGenerating...\n")

        response = engine.generate(prompt)

        print("\n" + "=" * 70)
        print(response)
        print("=" * 70)