from flask import request
from flask_restful import Resource
from ..models.usuario import Usuario as UsuarioModel

class login(Resource):
    # POST: loguear un usuario
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        usuario = UsuarioModel.query.filter_by(email=email, contraseña=password).first()
        
        if usuario:
            return {
                'message': 'Login exitoso',
                'rol': usuario.rol,
                'token': 'token-simulado-xyz' 
            }, 200
        
        return {'message': 'credenciales incorrectas'}, 401