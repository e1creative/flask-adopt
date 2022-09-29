"""Models for Adopt."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)


class Pet(db.Model):
    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)
    name = db.Column(db.String(20),
                     nullable=False)
    species = db.Column(db.String(50),
                        nullable=False)
    image_url = db.Column(db.Text)
    age = db.Column(db.Integer)
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean,
                          nullable=False)

    def __repr__(self):
        """Show Info about pet"""
        p = self
        return f"<Pet id={p.id} name={p.name} species={p.species} image_url={p.image_url} age={p.age} notes={p.notes} available={p.available} >"