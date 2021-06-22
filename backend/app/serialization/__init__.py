from app                 import api
from flask_restplus      import fields

# Login
model_login = api.model('Login',{
    'username' : fields.String(required=True),
    'password' : fields.String(required=True),
    'cellphone': fields.String(required=True),
})

# Player
player_user = api.model('Player',{
    'username' : fields.String,
    'picture'  : fields.String,
    'cellphone': fields.String,
    'stars'    : fields.Integer,
    'type'     : fields.String,
})

# Admin
admin_user = api.model('Admin',{
    'username' : fields.String,
    'picture'  : fields.String,
    'cellphone': fields.String,
    'password' : fields.String,
    'stars'    : fields.Integer,
    'type'     : fields.String,
})

# TEAM
model_team = api.model('Team',{
    'name'     : fields.String,
    'picture'  : fields.String,
    'color'    : fields.String,
})