from pab import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre1 = db.Column(db.String(40), nullable=False)
    tel1 = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    nombre2 = db.Column(db.String(20), nullable=False)
    tel2 = db.Column(db.String(20), nullable=False)
    cat = db.Column(db.String(20), nullable=False)

