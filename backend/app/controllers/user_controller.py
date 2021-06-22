from app.services.user_service     import UserService
from flask_restplus                import Resource
from app.routes                    import player_route
from app.serialization             import admin_user, player_user
from app.utils.oauth               import login_required   

@player_route.route('/player')
@player_route.response(404, 'Route not found')
@player_route.response(500, ';(')
class PlayerController(Resource):
    @player_route.expect(player_user)
    #@login_required
    def post(self):
        return UserService.save_player(player_route.payload)

@player_route.route('/admin')
@player_route.response(404, 'Route not found')
@player_route.response(500, ';(')
class AdminController(Resource):
    @player_route.expect(admin_user)
    #@login_required
    def post(self):
        return UserService.save_admin(player_route.payload)
       
player_route.add_resource(PlayerController, '/player', methods=['POST','GET','PUT'])
player_route.add_resource(AdminController, '/admin', methods=['POST','GET','PUT'])