from flask import request
from flask_restful import Resource

USUARIOS = {}

class Register(Resource):


    def post(self):
        data = request.get_json()

        nuevo_id = int(max(USUARIOS.keys())) + 1 if USUARIOS else 1
        USUARIOS[nuevo_id] = {
            'email': data.get('email'),
            'password': data.get('password'),
            'rol': data.get('rol', 'USER') 
        }
        return {'message': 'Usuario registrado con éxito', 'usuario': USUARIOS[nuevo_id]}, 201