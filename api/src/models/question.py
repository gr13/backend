from src.db import db


class QuestionModel(db.Model):
    __tablename__ = "questions"

    id = db.Column(db.Integer, primary_key=True)
    level_id = db.Column(db.Integer, nullable=False)
    difficulty_id = db.Column(db.Integer, nullable=False)
    chapter_id = db.Column(db.Integer, nullable=False)
    sub_chapter_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.String(255), nullable=False)
    image_file = db.Column(db.String(20), nullable=False)
    answer_a = db.Column(db.String(255), nullable=False)
    answer_b = db.Column(db.String(255), nullable=False)
    answer_c = db.Column(db.String(255), nullable=False)
    answer_d = db.Column(db.String(255), nullable=False)
    answer_time = db.Column(db.Integer, nullable=False, default=60)
    correct_answer = db.Column(db.String(1), nullable=False)
    correct_answer_text = db.Column(db.String(255), nullable=False)
    answer_img = db.Column(db.String(20), nullable=False)
    is_validated = db.Column(db.Boolean(), default=0)

    # lazy="dynamic" does not create the list of items
    # unless it is necessary
    # users = db.relationship(
    #     "UserModel", lazy="dynamic", back_populates="questions"
    # )

    def __init__(self, user_right):
        self.user_right = user_right

    def json(self):
        return {
            "id": self.id,
            "right": self.user_right
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    # @classmethod
    # def find_by_right(cls, right):
    #     return cls.query.filter_by(user_right=right).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
