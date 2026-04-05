from flask import request
from flask_restful import Resource

class Logout(Resource):
    # POST: invalida token actual 
    # Roles permitidos: USER, ADMIN, ENCARGADO 
    def post(self):
        # En una app real, aquí borrarías el token de la sesión o lo pondrías en una lista negra
        return {'message': 'Sesión cerrada correctamente. Token invalidado.'}, 200 