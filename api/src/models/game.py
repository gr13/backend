from src.db import db


class GameModel(db.Model):
    __tablename__ = "games"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, nullable=True)
    game_uid = db.Column(db.Integer, nullable=False)
    game_description = db.Column(db.String(255), nullable=False)
    recommend = db.Column(db.Boolean(), default=0)
    approved = db.Column(db.Boolean(), default=0)
    approved_user_id = db.Column(db.Integer, nullable=False)
    is_random = db.Column(db.Boolean(), default=0)
    is_multiplayer = db.Column(db.Boolean(), default=0)
    number_of_questions = db.Column(db.Integer, nullable=False, default=15)

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
            "user_id": self.user_id,
            "game_uid": self.game_uid,
            "game_description": self.game_description,
            "recommend": self.recommend,
            "approved": self.approved,
            "approved_user_id": self.approved_user_id,
            "is_random": self.is_random,
            "is_multiplayer": self.is_multiplayer,
            "number_of_questions": self.number_of_questions,
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_game_uid(cls, game_uid):
        return cls.query.filter_by(game_uid=game_uid).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
