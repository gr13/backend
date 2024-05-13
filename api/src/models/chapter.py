from src.db import db
from src.models.sub_chapter import SubChapterModel # noqa: E261, F401


class ChapterModel(db.Model):
    __tablename__ = "chapters"

    id = db.Column(db.Integer, primary_key=True)
    chapter = db.Column(db.Integer, nullable=False, unique=True)
    chapter_name = db.Column(db.String(255), unique=True)

    # lazy="dynamic" does not create the list of items
    # unless it is necessary
    sub_chapters = db.relationship(
        "SubChapterModel", back_populates="chapter", lazy="dynamic",
    )

    def __init__(self, user_right):
        self.user_right = user_right

    def json(self):
        return {
            "id": self.id,
            "chapter": self.chapter,
            "chapter_name": self.chapter_name,
            "sub_chapters": [
                sub_chapter.json() for sub_chapter in self.sub_chapters
            ],
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_chapter(cls, chapter: int):
        return cls.query.filter_by(chapter=chapter).first()

    # def save_to_db(self):
    #     db.session.add(self)
    #     db.session.commit()
