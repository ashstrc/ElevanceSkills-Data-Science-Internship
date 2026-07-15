import spacy


class ConceptExtractor:

    def __init__(self):

        self.nlp = spacy.load("en_core_web_sm")

        self.stop_words = {

            "a", "an", "the",

            "this", "that", "these", "those",

            "it", "its", "they", "their",

            "them", "he", "she", "you",

            "we", "our", "your",

            "what", "which", "who",

            "type", "way", "thing",

            "approach", "method",

            "system", "systems",

            "ability", "abilities",

            "time"

        }

    def extract(self, text):

        doc = self.nlp(text)

        concepts = []

        for chunk in doc.noun_chunks:

            phrase = chunk.text.strip()

            words = []

            for word in phrase.split():

                word = word.strip()

                if word.lower() in self.stop_words:
                    continue

                words.append(word)

            phrase = " ".join(words).strip()

            if len(phrase) < 4:
                continue

            if len(phrase.split()) > 4:
                continue

            if phrase.lower() in self.stop_words:
                continue

            concepts.append(
                phrase.title()
            )

        # Remove duplicates
        concepts = list(dict.fromkeys(concepts))

        # Keep only the first 12 concepts
        concepts = concepts[:12]

        return concepts


if __name__ == "__main__":

    extractor = ConceptExtractor()

    explanation = """
    Machine Learning is a branch of Artificial Intelligence.
    It enables computers to learn from data.
    Recommendation systems use Machine Learning.
    Healthcare and Finance are common applications.
    """

    concepts = extractor.extract(explanation)

    print()

    print("Extracted Concepts\n")

    for concept in concepts:

        print("•", concept)