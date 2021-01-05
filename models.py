from app import db


class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)