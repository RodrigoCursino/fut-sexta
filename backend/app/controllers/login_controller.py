from app.services.login_service    import LoginService
from flask_restplus                import Resource
from app.routes                    import login_route
from app.serialization             import model_login

@login_route.route('/')
@login_route.response(404, 'Route not found')
@login_route.response(500, ';(')
class LoginController(Resource):
    @login_route.expect(model_login)
    def post(self):
        return LoginService.login(login_route.payload)
       
login_route.add_resource(LoginController, '/', methods=['POST'])