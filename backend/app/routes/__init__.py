from app import api

#register route
register_route = api.namespace('register', description='User Register')

#login route
login_route    = api.namespace('login', description='User Authentication')

#player route
player_route    = api.namespace('users-register', description='Users Manager')

#teams route
team_route    = api.namespace('teams', description='Teams Manager')