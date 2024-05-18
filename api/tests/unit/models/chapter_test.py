import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
from src.models.chapter import ChapterModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class ChapterTest(BaseTest):

    def test_chapter_json(self):
        """
        Creates user model and checks the returned json
        """
        with self.app_context():
            chapter = ChapterModel.find_by_id(1)
            expected = {
                "id": 1,
                "chapter": 1,
                "chapter_name": "Roles and Responsibilities",
                "hide": False,
                "sub_chapters": [
                    {"id": 1, "chapter_id": 1, "sub_chapter": 0, "sub_chapter_name": "All", "hide": False},  # noqa:E501
                    {"id": 2, "chapter_id": 1, "sub_chapter": 1, "sub_chapter_name": "The Emergency Medical System", "hide": False},  # noqa:E501
                    {"id": 3, "chapter_id": 1, "sub_chapter": 2, "sub_chapter_name": "Legal and Ethical Issues", "hide": False},  # noqa:E501
                    {"id": 4, "chapter_id": 1, "sub_chapter": 3, "sub_chapter_name": "Communication", "hide": False},  # noqa:E501
                    {"id": 5, "chapter_id": 1, "sub_chapter": 4, "sub_chapter_name": "Documentation and Record Keeping", "hide": False}  # noqa:E501
                ]
            }
            actual: Dict = chapter.json()
            self.assertDictEqual(actual, expected,
                f"User JSON is incorrect expected: {expected}, actual: "
                    "{actual}")
