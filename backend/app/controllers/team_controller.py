from app.services.team_service     import TeamService
from flask_restplus                import Resource
from app.routes                    import team_route
from app.utils.oauth               import login_required   
from app.serialization             import model_team

@team_route.route('/')
@team_route.response(404, 'Route not found')
@team_route.response(500, ';(')
class TeamController(Resource):
    #@login_required
    @team_route.marshal_with(model_team)
    def get(self):
        try:
            return TeamService.list_all(), 200
        except Exception as e:
            return {"msg": "Key error"}, 404

       
team_route.add_resource(TeamController, '/', methods=['POST','GET','PUT'])