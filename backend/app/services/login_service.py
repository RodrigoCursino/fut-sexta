from app.utils.oauth        import create_token
from app.models.users       import User
from app                    import db
from app                    import bcrypt
from sqlalchemy             import exc 

class LoginService():
    
    @staticmethod
    def login(payload):
        user  = User.query.filter_by(cellphone=payload['cellphone']).first()
        token = ""
        if(user and bcrypt.check_password_hash(user.password, payload['password'])):
            token = create_token(user)
            
            return {
                'token' : str(token, 'utf-8'),
                'user'  : user.username,
                'cellphone' : user.cellphone,
            }, 200
           
        return {
            'message': 'Senha ou celular não estão corretos'
        }, 401

    
    @staticmethod
    def register(payload):
        try:
            if(not User.query.filter_by(cellphone=payload['cellphone']).first()):
                user = User(payload['username'], payload['picture'],payload['stars'], payload['name'], payload['cellphone'], ['password'])
                db.session.add(user)
                db.session.commit()

                return {"message": "sucesso ao inserir usuário"}, 201
            
            return {"message": "Usuário já cadastrado"}, 422 
            
        except exc.SQLAlchemyError as e:
            db.session.rollback()
            return {"message": "Todos eram até o nosso servidor :("}, 500