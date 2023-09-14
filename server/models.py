from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    image = db.Column(db.String)
    price = db.Column(db.Integer)
    # published_at = db.Column(db.DateTime, server_default=db.func.now())
    # edited_at = db.Column(db.DateTime, onupdate=db.func.now())

    def __repr__():
        return f'{db.id}, {db.name}, {db.image}, {db.price}'
