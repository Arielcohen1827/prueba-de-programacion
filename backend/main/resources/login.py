from flask import request
from flask_restful import Resource

USUARIOS = {
    1: {'email': 'manuel@gmail.com', 'password': '123', 'rol': 'ADMIN'},
    2: {'email': 'pepe@gmail.com', 'password': '123', 'rol': 'USER'}
}

class login(Resource):
    # POST: loguear un usuario
  
    def post(self):
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        # buscamos si el usuario existe y la contraseña coincide
        for id, datos in USUARIOS.items():
            if datos['email'] == email and datos['password'] == password: 
                return {
                    'message': 'Login exitoso',
                    'rol': datos['rol'],
                    'token': 'token-simulado-xyz' 
                }, 200
        
        return {'message': 'credenciales incorrectas'}, 401