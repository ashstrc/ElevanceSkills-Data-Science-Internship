from transformers import pipeline


class PaperSummarizer:

    def __init__(self):

        print("Loading Summarization Model...")

        self.summarizer = pipeline(
            task="summarization",
            model="sshleifer/distilbart-cnn-12-6"
        )

        print("Summarizer Ready!")

    def summarize(self, text):

        input_words = len(text.split())

        max_length = min(120, max(40, input_words // 2))

        summary = self.summarizer(
            text[:2000],
            max_length=max_length,
            min_length=30,
            do_sample=False
            )

        return summary[0]["summary_text"]


if __name__ == "__main__":

    summarizer = PaperSummarizer()

    text = input("\nPaste Research Abstract:\n\n")

    print("\nGenerating Summary...\n")

    summary = summarizer.summarize(text)

    print("\nSummary:\n")

    print(summary)