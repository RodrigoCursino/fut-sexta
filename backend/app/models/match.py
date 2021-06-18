from app  import db

class Match(db.Model):
    __tablename__         = "matches"
    id                    = db.Column(db.Integer, primary_key=True, autoincrement=True)
    id_team_one           = db.Column(db.ForeignKey('teams_players.id'), primary_key=True)
    id_team_two           = db.Column(db.ForeignKey('teams_players.id'), primary_key=True)
    # [VITORIA,EMPATE,DERROTA]
    match_status_team_one = db.Column(db.String(25))
    match_status_team_two = db.Column(db.String(25))
    match_date            = db.Column(db.DateTime)
    activate              = db.Column(db.Boolean, default=True)

    def __init__(self, id_team_one, id_team_two, match_status_team_one, match_status_team_two, match_date, activate):
        self.id_team_one  = id_team_one 
        self.id_team_two  = id_team_two 
        self.match_status_team_one = match_status_team_one  
        self.match_status_team_two = match_status_team_two   
        self.match_date   = match_date
        self.activate     = activate     
         
    def __repr__(self):
        return "<MATCH %r>" % self.match_date