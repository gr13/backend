from src.db import db


class SubChapterModel(db.Model):
    __tablename__ = "sub_chapters"

    id = db.Column(db.Integer, primary_key=True)
    chapter_id = db.Column(
        db.Integer,
        db.ForeignKey("chapters.id"),
        nullable=False,
    )
    sub_chapter = db.Column(db.Integer, nullable=False, unique=True)
    sub_chapter_name = db.Column(db.String(255), unique=True)

    # lazy="dynamic" does not create the list of items
    # unless it is necessary
    # chapter = db.relationship(
    #     "ChapterModel", back_populates="sub_chapters", lazy="dynamic"
    # )

    chapter = db.relationship("ChapterModel")

    def __init__(self, user_right):
        self.user_right = user_right

    def json(self):
        return {
            "id": self.id,
            "chapter": self.chapter,
            "sub_chapter": self.sub_chapter,
            "sub_chapter_name": self.sub_chapter_name,
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
