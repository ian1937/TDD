from app import db


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String)

    def __repr__(self):
        return self.text