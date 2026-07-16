import os
import torch
import time

os.environ["HF_HOME"] = r"D:\hf_cache"
os.environ["HF_HUB_CACHE"] = r"D:\hf_cache"

from transformers import (
    AutoProcessor,
    Qwen2_5_VLForConditionalGeneration
)

from qwen_vl_utils import process_vision_info


MODEL_PATH = (
    r"D:\hf_cache\models--Qwen--Qwen2.5-VL-3B-Instruct"
    r"\snapshots"
)


def find_snapshot():

    if not os.path.exists(MODEL_PATH):
        raise FileNotFoundError(MODEL_PATH)

    folders = os.listdir(MODEL_PATH)

    if len(folders) == 0:
        raise Exception("Snapshot not found.")

    return os.path.join(MODEL_PATH, folders[0])


class ImageAnalyzer:

    def __init__(self):

        print("Loading Qwen2.5-VL Vision Engine...")

        self.device = "cuda" if torch.cuda.is_available() else "cpu"

        self.model_path = find_snapshot()

        self.processor = AutoProcessor.from_pretrained(
            self.model_path,
            local_files_only=True
        )

        self.model = Qwen2_5_VLForConditionalGeneration.from_pretrained(
            self.model_path,
            torch_dtype=torch.float32,
            local_files_only=True
        )

        self.model.to(self.device)
        self.model.eval()

        print("Qwen2.5-VL Ready!")

    # --------------------------------------------------------

    def extract_visual_evidence(self, image_path):

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "image",
                        "image": image_path
                    },
                    {
                        "type": "text",
                        "text": """
Analyze the image carefully.

Return ONLY observable evidence.

Use this format exactly.

Objects:
Animals:
People:
Environment:
Colors:
Activities:
Visible Text:
Important Details:

Do not answer any question.
Do not infer invisible facts.
Do not explain.
Only return visual evidence.
"""
                    }
                ]
            }
        ]

        text = self.processor.apply_chat_template(
            messages,
            tokenize=False,
            add_generation_prompt=True
        )

        image_inputs, video_inputs = process_vision_info(messages)

        inputs = self.processor(
            text=[text],
            images=image_inputs,
            videos=video_inputs,
            padding=True,
            return_tensors="pt"
        )

        inputs = {
            k: v.to(self.device)
            if hasattr(v, "to")
            else v
            for k, v in inputs.items()
        }

        with torch.no_grad():
            
            start = time.time()

            generated_ids = self.model.generate(
                **inputs,
                max_new_tokens=96,
                do_sample=False
            )
            print(f"Inference Time: {time.time() - start:.2f} seconds")

        generated_ids_trimmed = [
            out_ids[len(in_ids):]
            for in_ids, out_ids
            in zip(inputs["input_ids"], generated_ids)
        ]

        output = self.processor.batch_decode(
            generated_ids_trimmed,
            skip_special_tokens=True,
            clean_up_tokenization_spaces=False
        )[0]

        return output.strip()


if __name__ == "__main__":

    analyzer = ImageAnalyzer()

    image = input("Image Path: ")

    print("\nExtracting Visual Evidence...\n")

    evidence = analyzer.extract_visual_evidence(image)

    print(evidence)