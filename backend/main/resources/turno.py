from flask import request, jsonify
from flask_restful import Resource
from datetime import datetime
from .. import db
from ..models.turno import Turno as TurnoModel

class Turno(Resource):
    # GET /turno/<id>
    def get(self, id):
        turno = db.session.query(TurnoModel).get_or_404(id)
        return turno.to_json(), 200

    # PUT /turno/<id>
    def put(self, id):
        turno = db.session.query(TurnoModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(turno, key, value)
        db.session.add(turno)
        db.session.commit()
        return turno.to_json(), 200

    # DELETE /turno/<id>
    def delete(self, id):
        turno = db.session.query(TurnoModel).get_or_404(id)
        db.session.delete(turno)
        db.session.commit()
        return {'message': 'Turno eliminado con éxito'}, 200

class Turnos(Resource):
    # GET /turnos
    def get(self):
        params = request.args
        query = db.session.query(TurnoModel)

        if 'fecha' in params:
            try:
                fecha = datetime.strptime(params['fecha'], '%d/%m/%Y').date()
                query = query.filter(TurnoModel.fecha == fecha)
            except ValueError:
                return {"message": "Formato de fecha inválido. Use DD/MM/YYYY."}, 400
        if 'hora' in params:
            try:
                hora = datetime.strptime(params['hora'], '%H:%M:%S').time()
                query = query.filter(TurnoModel.hora == hora)
            except ValueError:
                return {"message": "Formato de hora inválido. Use HH:MM:SS."}, 400
        if 'estado' in params:
            estado = params.get('estado', '').strip()
            query = query.filter(TurnoModel.estado.ilike(f"%{estado}%"))

        return jsonify({'turnos': [turno.to_json() for turno in query.all()]})

    # POST /turnos
    def post(self):
        turno = TurnoModel.from_json(request.get_json())
        db.session.add(turno)
        db.session.commit()
        return turno.to_json(), 201
