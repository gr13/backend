# import logging
from src.db import db
from src.models.user_right import UserRightModel # noqa
from sqlalchemy.orm import validates
from werkzeug.security import generate_password_hash, check_password_hash

import secrets


class UserModel(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(256))
    right_id = db.Column(
        db.Integer,
        db.ForeignKey("rights.id"),
        unique=False,
        nullable=False,
        default=1
    )
    right = db.relationship(
        "UserRightModel",
        back_populates="users",
    )

    username = db.Column(db.String(10), default="")
    position = db.Column(db.String(100), default="")

    can_validate = db.Column(db.Boolean(), default=False)
    can_edit = db.Column(db.Boolean(), default=False)
    can_seelog = db.Column(db.Boolean(), default=False)
    can_seeusers = db.Column(db.Boolean(), default=False)

    hide = db.Column(db.Boolean(), default=False)

    @validates("email")
    def validate_email(self, key, email):
        assert "@" in email
        return email

    def __init__(self, **kwargs):
        self.email = kwargs["email"]
        self.username = kwargs["username"]
        self.password = self.set_password(kwargs["password"])
        self.right_id = 2
        self.position = "Not in use"
        self.can_validate = False
        self.can_edit = False
        self.can_seelog = False
        self.can_seeusers = False
        self.hide = False

    def json(self):
        # right = UserRightModel.find_by_id(self.right_id)
        return {
            "id": self.id,
            "email": self.email,
            "right_id": self.right_id,
            "right": self.right.json() if self.right else None,
            "username": self.username,
            "can_validate": self.can_validate,
            "can_edit": self.can_edit,
            "can_seelog": self.can_seelog,
            "can_seeusers": self.can_seeusers,
            "hide": self.hide
        }

    @classmethod
    def find_by_email(cls, email: str):
        return cls.query.filter_by(email=email).first()

    @classmethod
    def find_by_id(cls, _id: int):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        # db.session.delete(self)
        # db.session.commit()
        self.hide = True
        self.save_to_db()

    def set_password(self, _password):
        return generate_password_hash(_password)

    def check_password(self, _password):
        return check_password_hash(self.password, _password)

    @classmethod
    def create_random_password(cls):
        return secrets.token_hex(8)
