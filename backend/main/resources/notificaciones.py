from flask import request, jsonify
from flask_restful import Resource
from datetime import datetime
from .. import db
from ..models.notificacion import Notificacion as NotificacionModel


class NotificacionesPaciente(Resource):
    # GET /paciente/<id>/notificaciones - Obtener una notificación por ID
    def get(self, paciente_id):
        # We assume paciente_id here was meant to be id_usuario because "notificacion" model points to "id_usuario"
        params = request.args
        query = db.session.query(NotificacionModel).filter_by(id_usuario=paciente_id) # Filtrar por paciente_id (id_usuario)
        if 'mensaje' in params:
            mensaje = params.get('mensaje', '').strip()
            query = query.filter(NotificacionModel.mensaje.ilike(f"%{mensaje}%"))
        if 'tipo' in params:
            tipo = params.get('tipo', '').strip()
            query = query.filter(NotificacionModel.tipo.ilike(f"%{tipo}%"))
        if 'leida' in params:
            leida = params.get('leida', '').strip()
            query = query.filter(NotificacionModel.leida == (leida == 'true'))
        if 'fecha' in params:
            try:
                fecha = datetime.strptime(params['fecha'], '%d/%m/%Y').date()
                query = query.filter(NotificacionModel.fecha == fecha)
            except ValueError:
                return {"message": "Formato de fecha inválido. Use DD/MM/YYYY."}, 400

        return jsonify({'notificaciones': [n.to_json() for n in query.all()]})

class Notificacion(Resource):
    # GET /notificacion/<id> - Obtener notificacion especifica
    def get(self, id):
        notificacion = db.session.query(NotificacionModel).get_or_404(id)
        return notificacion.to_json(), 200
        
    # PUT /notificacion/<id> - Actualizar notificacion
    def put(self, id):
        notificacion = db.session.query(NotificacionModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(notificacion, key, value)
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 200
        
    # DELETE /notificacion/<id> - Borrar notificacion
    def delete(self, id):
        notificacion = db.session.query(NotificacionModel).get_or_404(id)
        db.session.delete(notificacion)
        db.session.commit()
        return {'message': 'Notificación eliminada con éxito'}, 200


class Notificaciones(Resource):
    # GET /notificaciones - Obtener todas las notificaciones
    def get(self):
        params = request.args
        query = db.session.query(NotificacionModel)
        if 'mensaje' in params:
            mensaje = params.get('mensaje', '').strip()
            query = query.filter(NotificacionModel.mensaje.ilike(f"%{mensaje}%"))
        if 'tipo' in params:
            tipo = params.get('tipo', '').strip()
            query = query.filter(NotificacionModel.tipo.ilike(f"%{tipo}%"))
        if 'leida' in params:
            leida = params.get('leida', '').strip()
            query = query.filter(NotificacionModel.leida == (leida == 'true'))
        if 'fecha' in params:
            try:
                fecha = datetime.strptime(params['fecha'], '%d/%m/%Y').date()
                query = query.filter(NotificacionModel.fecha == fecha)
            except ValueError:
                return {"message": "Formato de fecha inválido. Use DD/MM/YYYY."}, 400

        notificaciones = query.all()
        return jsonify({'notificaciones': [n.to_json() for n in notificaciones]})

    # POST /notificaciones - Crear una nueva notificacion
    def post(self):
        notificacion = NotificacionModel.from_json(request.get_json())
        db.session.add(notificacion)
        db.session.commit()
        return notificacion.to_json(), 201
