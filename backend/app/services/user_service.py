from app.models.users       import User
from app.models.roles_users import RoleUser
from app.models.roles       import Role
from app                    import db

class UserService():

    @staticmethod
    def save_admin(payload):
        
        _type = 'AVULSO'
        if payload['type'] == 'MENSAL':
            _type = 'MENSAL'

        user = User(payload['username'], payload['picture'], payload['stars'], _type, payload['cellphone'], payload['password'])
        role = Role.query.filter(Role.name=='ADMIN').first()
        db.session.add(user)
        role_user = RoleUser(user,role)
        db.session.add(role_user)
        db.session.commit()

        return {"message": "sucesso ao inserir admin"}, 201
    
    @staticmethod
    def save_player(payload):
        
        _type = 'AVULSO'
        if payload['type'] == 'MENSAL':
            _type = 'MENSAL'

        user = User(payload['username'], payload['picture'], payload['stars'], _type, payload['cellphone'], payload['cellphone'])
        role = Role.query.filter(Role.name=='PLAYER').first()
        db.session.add(user)
        role_user = RoleUser(user,role)
        db.session.add(role_user)
        db.session.commit()

        return {"message": "sucesso ao inserir usuário"}, 201