from src.db import db


class UserRightModel(db.Model):
    __tablename__ = "rights"

    id = db.Column(db.Integer, primary_key=True)
    user_right = db.Column(db.String(20), unique=True)

    # lazy="dynamic" does not create the list of items
    # unless it is necessary
    users = db.relationship(
        "UserModel",
        back_populates="right",
        lazy="dynamic"
    )

    def __init__(self, user_right):
        self.user_right = user_right

    def json(self):
        return {
            "id": self.id,
            "right": self.user_right
        }

    def get_users_json(self):
        return {
            "users": [user.json() for user in self.users],
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_right(cls, right: str):
        return cls.query.filter_by(user_right=right).first()

    @classmethod
    def get_users(cls):
        return cls.users

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
