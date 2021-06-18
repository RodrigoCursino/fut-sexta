from app               import db, bcrypt, app

class Team(db.Model):
    __tablename__ = "teams"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.String(100))
    color      = db.Column(db.String(50))
    picture    = db.Column(db.String(800))
    activate   = db.Column(db.Boolean, default=True)

    def __init__(self, name, color, picture, activate=True):
        self.name     = name
        self.color    = color
        self.picture  = picture
        self.activate = activate