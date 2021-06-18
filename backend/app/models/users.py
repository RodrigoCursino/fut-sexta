from app               import db, bcrypt, app

class User(db.Model):
    __tablename__ = "users"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username   = db.Column(db.String(100))
    picture    = db.Column(db.String(800))
    stars      = db.Column(db.Integer)
    name       = db.Column(db.String(100))
    cellphone  = db.Column(db.String(20), unique=True)
    password   = db.Column(db.String(255))
    activate   = db.Column(db.Boolean, default=True)

    def __init__(self, username, picture, stars, name, cellphone, password, activate=True):
        self.username  = username
        self.picture   = picture
        self.stars     = stars
        self.name      = name
        self.cellphone = cellphone
        self.activate  = activate
        self.password  = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()