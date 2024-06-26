import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
from src.models.question import QuestionModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class QuestionTest(BaseTest):
    @staticmethod
    def _create_question() -> QuestionModel:
        """
        Creates a question to be used in tests
        """
        return QuestionModel(
            level_id=1,
            difficulty_id=1,
            chapter_id=1,
            sub_chapter_id=1,
            question="question",
            image_file="",
            answer_1="answ a",
            answer_2="answ b",
            answer_3="answ c",
            answer_4="answ d",
            answer_time=60,
            correct_answer=1,
            correct_answer_text="correct Answer",
            answer_img="",
            is_validated=False,
        )

    def test_create_question(self):
        """
        Creates model and checks that question is correct
        """
        question = self._create_question()
        self.assertEqual(question.question, "question",
            "The question of the question after creation does not equal"
            " the constructor argument.")
        self.assertEqual(question.answer_1, "answ a",
            "The answer_1 of the question after creation does not "
            "equal the constructor argument.")

    def test_questions_json(self):
        """
        Creates a question model and checks the returned json
        """
        question = self._create_question()
        expected = {
            "id": None,
            "level_id": 1,
            "difficulty_id": 1,
            "chapter_id": 1,
            "sub_chapter_id": 1,
            "question": "question",
            "image_file": "",
            "answer_1": "answ a",
            "answer_2": "answ b",
            "answer_3": "answ c",
            "answer_4": "answ d",
            "answer_time": 60,
            "correct_answer": 1,
            "correct_answer_text":
            "correct Answer",
            "answer_img": "",
            "is_validated": False,
            "level": None,
            "difficulty": None,
            "chapter": None,
            "sub_chapter": None,
            "is_error": False,
            "hide": False,
        }
        actual: Dict = question.json()
        self.assertDictEqual(actual, expected,
            f"Question JSON is incorrect expected: {expected}, actual: "
                "{actual}")
