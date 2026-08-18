import unittest
from pathlib import Path

from streamlit.testing.v1 import AppTest


ROOT_DIR = Path(__file__).parent.parent.parent
WEBUI_MAIN = ROOT_DIR / "webui" / "Main.py"
HELP_IMAGES = ROOT_DIR / "webui" / "help" / "images"


class TestWebuiHelpPage(unittest.TestCase):
    def test_help_page_opens_from_session_state(self):
        app = AppTest.from_file(str(WEBUI_MAIN), default_timeout=30)
        app.session_state["ui_language"] = "en"
        app.session_state["help_page_open"] = True
        app.session_state["help_query_handled"] = True
        app.run()

        self.assertFalse(app.exception)
        markdown = "\n".join(str(item.value) for item in app.markdown)
        self.assertIn("How to get started", markdown)
        self.assertIn("B-roll", markdown)
        self.assertIn("Connect an AI model", markdown)
        button_labels = [item.label for item in app.button]
        self.assertTrue(any("Back to Studio" in label for label in button_labels))
        self.assertFalse(any(label == "Generate Video" for label in button_labels))

    def test_studio_is_the_default_view(self):
        app = AppTest.from_file(str(WEBUI_MAIN), default_timeout=30)
        app.session_state["ui_language"] = "en"
        app.session_state["help_query_handled"] = True
        app.run()

        self.assertFalse(app.exception)
        button_labels = [item.label for item in app.button]
        self.assertTrue(any("Help" in label for label in button_labels))
        self.assertTrue(any("Generate Video" in label for label in button_labels))

    def test_help_images_are_shipped(self):
        required = ("overview.png", "settings-llm.png", "settings-materials.png")
        missing = [name for name in required if not (HELP_IMAGES / name).is_file()]
        self.assertEqual(missing, [])


if __name__ == "__main__":
    unittest.main()
