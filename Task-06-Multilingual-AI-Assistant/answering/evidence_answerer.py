import re


class EvidenceAnswerer:
    """
    Answers simple factual questions directly from the extracted scene.

    This module NEVER uses an LLM.
    It only returns information already present in the scene.
    """

    def __init__(self):
        pass

    # ---------------------------------------------------------

    def answer(self, question: str, scene: dict):

        q = question.lower().strip()

        q = re.sub(r"[^\w\s]", "", q)

        # -------------------------------------------------
        # Animal
        # -------------------------------------------------

        if any(word in q for word in [
            "animal",
            "species",
            "creature"
        ]):

            animals = scene.get("animals", [])

            if animals:
                return f"The animal is {', '.join(animals)}."

            return "No animals were detected."

        # -------------------------------------------------
        # People
        # -------------------------------------------------

        if any(word in q for word in [
            "person",
            "people",
            "human",
            "man",
            "woman",
            "boy",
            "girl"
        ]):

            people = scene.get("people", [])

            if people:
                return f"Detected people: {', '.join(people)}."

            return "No people were detected."

        # -------------------------------------------------
        # Objects
        # -------------------------------------------------

        if any(word in q for word in [
            "object",
            "objects",
            "thing",
            "things"
        ]):

            objects = scene.get("objects", [])

            if objects:
                return f"Detected objects: {', '.join(objects)}."

            return "No objects were detected."

        # -------------------------------------------------
        # Activity
        # -------------------------------------------------

        if any(word in q for word in [
            "doing",
            "activity",
            "activities",
            "action"
        ]):

            activities = scene.get("activities", [])

            if activities:
                return f"The detected activity is {', '.join(activities)}."

            return "No activity was detected."

        # -------------------------------------------------
        # Colors
        # -------------------------------------------------

        if any(word in q for word in [
            "color",
            "colors",
            "colour",
            "colours"
        ]):

            colors = scene.get("colors", [])

            if colors:
                return f"The visible colors are {', '.join(colors)}."

            return "No colors were detected."

        # -------------------------------------------------
        # Environment
        # -------------------------------------------------

        if any(word in q for word in [
            "environment",
            "background",
            "location",
            "place",
            "where"
        ]):

            environment = scene.get("environment", "")

            if environment:
                return f"The environment appears to be {environment}."

            return "The environment could not be determined."

        # -------------------------------------------------
        # Visible Text
        # -------------------------------------------------

        if any(word in q for word in [
            "text",
            "written",
            "writing",
            "words"
        ]):

            text = scene.get("visible_text", "")

            if text and text.lower() != "none":
                return f"Visible text: {text}"

            return "No visible text was detected."

        # -------------------------------------------------
        # Details
        # -------------------------------------------------

        if any(word in q for word in [
            "detail",
            "details"
        ]):

            details = scene.get("details", "")

            if details:
                return details

            return "No additional details are available."

        # -------------------------------------------------
        # Count
        # -------------------------------------------------

        if "how many" in q:

            if "animal" in q:
                return f"{len(scene.get('animals', []))} animal(s) detected."

            if "person" in q or "people" in q:
                return f"{len(scene.get('people', []))} person(s) detected."

            if "object" in q:
                return f"{len(scene.get('objects', []))} object(s) detected."

        # -------------------------------------------------
        # Unknown
        # -------------------------------------------------

        return None