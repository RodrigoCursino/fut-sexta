from app               import db, bcrypt, app

class Role(db.Model):
    __tablename__ = "roles"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name       = db.Column(db.String(100))
    activate   = db.Column(db.Boolean, default=True)

    def __init__(self, name, activate=True):
        self.name     = name
        self.activate = activate