import re


class SceneBuilder:
    """
    Converts the raw output of the Vision Model into a structured scene.

    The rest of the assistant never parses raw text.
    It only works with the Scene object.
    """

    def __init__(self):
        pass

    # -------------------------------------------------------------

    def build_scene(self, evidence: str):

        scene = {
            "animals": [],
            "people": [],
            "objects": [],
            "environment": "",
            "activities": [],
            "colors": [],
            "visible_text": "",
            "details": ""
        }

        current_section = None

        for line in evidence.splitlines():

            line = line.strip()

            if not line:
                continue

            lower = line.lower()

            # -------------------------
            # Detect Section Headers
            # -------------------------

            if lower.startswith("animals"):
                current_section = "animals"

                value = line.split(":", 1)

                if len(value) > 1:
                    self._append(scene["animals"], value[1])

                continue

            if lower.startswith("people"):
                current_section = "people"

                value = line.split(":", 1)

                if len(value) > 1:
                    self._append(scene["people"], value[1])

                continue

            if lower.startswith("objects"):
                current_section = "objects"

                value = line.split(":", 1)

                if len(value) > 1:
                    self._append(scene["objects"], value[1])

                continue

            if lower.startswith("environment"):
                current_section = "environment"

                value = line.split(":", 1)

                if len(value) > 1:
                    scene["environment"] = value[1].strip()

                continue

            if lower.startswith("activities"):
                current_section = "activities"

                value = line.split(":", 1)

                if len(value) > 1:
                    self._append(scene["activities"], value[1])

                continue

            if lower.startswith("colors"):
                current_section = "colors"

                value = line.split(":", 1)

                if len(value) > 1:
                    self._append(scene["colors"], value[1])

                continue

            if lower.startswith("visible text"):
                current_section = "visible_text"

                value = line.split(":", 1)

                if len(value) > 1:
                    scene["visible_text"] = value[1].strip()

                continue

            if lower.startswith("important details"):
                current_section = "details"

                value = line.split(":", 1)

                if len(value) > 1:
                    scene["details"] = value[1].strip()

                continue

            # -------------------------
            # Bullet Points
            # -------------------------

            if line.startswith("-"):

                value = line[1:].strip()

                if current_section == "animals":
                    scene["animals"].append(value)

                elif current_section == "people":
                    scene["people"].append(value)

                elif current_section == "objects":
                    scene["objects"].append(value)

                elif current_section == "activities":
                    scene["activities"].append(value)

                elif current_section == "colors":
                    scene["colors"].append(value)

        return scene

    # -------------------------------------------------------------

    def _append(self, target, text):

        text = text.strip()

        if not text:
            return

        if text.lower() == "none":
            return

        items = re.split(r",\s*", text)

        for item in items:

            item = item.strip()

            if item and item.lower() != "none":
                target.append(item)