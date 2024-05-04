from src.db import db


class GameQuestionModel(db.Model):
    __tablename__ = "game_questions"

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, nullable=False)
    question_id = db.Column(db.Integer, nullable=False)
    question_order = db.Column(db.Integer, nullable=False)

    # lazy="dynamic" does not create the list of items
    # unless it is necessary
    # users = db.relationship(
    #     "UserModel", lazy="dynamic", back_populates="rights"
    # )

    def __init__(self, user_right):
        self.user_right = user_right

    def json(self):
        return {
            "id": self.id,
            "game_id": self.game_id,
            "question_id": self.question_id,
            "question_order": self.question_order,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_game(cls, game_id):
        return cls.query.filter_by(game_id=game_id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()