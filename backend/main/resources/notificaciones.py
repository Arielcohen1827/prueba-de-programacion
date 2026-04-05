from flask import request
from flask_restful import Resource


NOTIFICACIONES = []

class notificacion(Resource):
    
    def post(self):
        data = request.get_json()
        

        nueva_notificacion = {
            'id_usuario': data.get('id_usuario'), # a quien va dirigida
            'mensaje': data.get('mensaje'),       # el contenido del aviso
            'tipo': data.get('tipo', 'general'),  # ej: 'turno', 'ejercicio', 'pago'
            'leida': False
        }
        
        NOTIFICACIONES.append(nueva_notificacion)
        
        return {
            'status': 'notificacion enviada con exito',
            'detalle': nueva_notificacion
        }, 201