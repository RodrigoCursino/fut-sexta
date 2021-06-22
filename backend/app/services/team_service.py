from app.models.teams       import Team
from app                    import db

class TeamService():

    @staticmethod
    def list_all():
        return list(Team.query.filter(Team.activate==True).all())
        
        