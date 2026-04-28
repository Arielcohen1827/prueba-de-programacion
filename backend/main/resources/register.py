from flask import request
from flask_restful import Resource
from .. import db
from ..models.usuario import Usuario as UsuarioModel

class Register(Resource):
    def post(self):
        data = request.get_json()

        # Check if email exists
        if UsuarioModel.query.filter_by(email=data.get('email')).first():
            return {'message': 'Email ya registrado'}, 400

        nuevo_usuario = UsuarioModel(
            email=data.get('email'),
            contraseña=data.get('password'),
            rol=data.get('rol', 'USER') 
        )
        
        db.session.add(nuevo_usuario)
        db.session.commit()
        
        return {'message': 'Usuario registrado con éxito', 'usuario': nuevo_usuario.to_json()}, 201