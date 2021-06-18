from app  import db

class Statistic(db.Model):
    __tablename__         = "statistics"
    id                    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_user               = db.Column(db.ForeignKey('users.id'), primary_key=True)
    # ['GOL', 'ASSSITENCIA', 'VITORIA', 'DERROTA', 'EMPATE']
    date                  = db.Column(db.DateTime)
    status                = db.Column(db.String(50))
    activate              = db.Column(db.Boolean, default=True)

    def __init__(self, id_user, date, status, activate):
        self.id_user  = id_user 
        self.date     = date 
        self.status   = status
        self.activate = activate     
         
    def __repr__(self):
        return "<STATISTICS %r>" % self.date