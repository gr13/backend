import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
from src.models.question_difficulty import QuestionDifficultyModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class QuestionLevelTest(BaseTest):

    def test_question_level_json(self):
        """
        Creates user model and checks the returned json
        """
        with self.app_context():
            right = QuestionDifficultyModel.find_by_id(1)
            expected = {"id": 1, "difficulty": 0, "difficulty_name": "warm up"}
            actual: Dict = right.json()
            self.assertDictEqual(actual, expected,
                f"User JSON is incorrect expected: {expected}, actual: "
                    "{actual}")
