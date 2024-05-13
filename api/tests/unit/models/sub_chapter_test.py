import sys
from typing import Dict
# adding src to the system path
from pathlib import Path
sys.path.append(str(Path(sys.path[0]).parent))
sys.path.append(str(Path(sys.path[0]).parent.parent))
sys.path.append(str(Path(sys.path[0]).parent.parent.parent))
from src.models.sub_chapter import SubChapterModel  # noqa:E402
from tests.base_test import BaseTest  # noqa:E402


class SubChapterTest(BaseTest):

    def test_chapter_json(self):
        """
        Creates user model and checks the returned json
        """
        with self.app_context():
            SubChapter = SubChapterModel.find_by_id(1)
            expected = {
                "id": 1,
                "chapter_id": 1,
                "sub_chapter": 0,
                "sub_chapter_name": "All"
            }
            actual: Dict = SubChapter.json()
            self.assertDictEqual(actual, expected,
                f"User JSON is incorrect expected: {expected}, actual: "
                    "{actual}")
