from app               import db, bcrypt, app

class User(db.Model):
    __tablename__ = "users"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username   = db.Column(db.String(100))
    picture    = db.Column(db.String)
    stars      = db.Column(db.Integer)
    type       = db.Column(db.String(10))
    cellphone  = db.Column(db.String(20), unique=True)
    password   = db.Column(db.String(255))
    activate   = db.Column(db.Boolean, default=True)

    def __init__(self, username, picture, stars, type, cellphone, password, activate=True):
        self.username  = username
        self.picture   = picture
        self.stars     = stars
        self.type      = type
        self.cellphone = cellphone
        self.activate  = activate
        self.password  = bcrypt.generate_password_hash(
            password, app.config.get('BCRYPT_LOG_ROUNDS')
        ).decode()