from app  import db

class TeamPlayer(db.Model):
    __tablename__     = "teams_players"
    id                = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_team           = db.Column(db.ForeignKey('teams.id'), primary_key=True)
    id_user           = db.Column(db.ForeignKey('users.id'), primary_key=True)
    date              = db.Column(db.DateTime)
    team              = db.relationship('Team', foreign_keys=id_team)
    player            = db.relationship('Player', foreign_keys=id_user)
    activate          = db.Column(db.Boolean, default=True)

    def __init__(self, id_team, id_user, date, activate):
          self.id_team  = id_team
          self.id_user  = id_user
          self.date     = date
          self.activate = activate
         
    def __repr__(self):
        return "<TeamPlayer %r>" % self.date