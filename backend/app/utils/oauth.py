import jwt
import datetime
from   functools              import wraps
from   flask                  import g, request, redirect, url_for
from   app                    import app
from   app.models.users       import User

def login_required(f):
    @wraps(f)
    def decode_auth_token(*args, **kwargs):
        """
        Decodes um auth token
        :param: request:
        :return: string
        """
        try:
            auth_token  = ""
            auth_header = request.headers.get('Authorization')
            
            if auth_header:
                auth_token = auth_header.split(" ")[1]

            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))   

            user = User.query.filter_by(id=payload['id'],cellphone=payload['cellphone']).first()         
    
            if user:
                return f(*args, **kwargs)
            else:
                return {"Mensagem":"Não Permitido"}, 401
        
        except jwt.ExpiredSignatureError:
            print('Signature expired. Please log in again.')
            return {"Mensagem":"Não Permitido"}, 401
        except jwt.InvalidTokenError:
            print('Invalid token. Please log in again.')
            return {"Mensagem":"Não Permitido"}, 401

    return decode_auth_token

def create_token(user):
        """
            Gerando auth token
            :retun: string
        """
        try:
            payload = {
                'exp'      : datetime.datetime.utcnow() + datetime.timedelta(days=1,seconds=30),
                'iat'      : datetime.datetime.utcnow(),
                'id'       : user.id,
                'cellphone': user.cellphone,
                'username' : user.username
            }

            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e
