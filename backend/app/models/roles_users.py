from app               import db, bcrypt, app

class RoleUser(db.Model):
    __tableid_role__ = "roles_users"
    id         = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_role    = db.Column(db.ForeignKey('roles.id'), primary_key=True)
    id_user    = db.Column(db.ForeignKey('users.id'), primary_key=True)
    role       = db.relationship('Role', foreign_keys=id_role)
    user       = db.relationship('User', foreign_keys=id_user)
    activate   = db.Column(db.Boolean, default=True)

    def __init__(self, user, role, activate=True):
        self.role     = role
        self.user     = user
        self.activate = activate