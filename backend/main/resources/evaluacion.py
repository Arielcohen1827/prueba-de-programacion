from flask import request, jsonify
from flask_restful import Resource
from datetime import datetime
from .. import db
from ..models.evaluacion import Evaluacion as EvaluacionModel

class Evaluacion(Resource):
    # GET /evaluacion/<id>
    def get(self, id):
        evaluacion = db.session.query(EvaluacionModel).get_or_404(id)
        return evaluacion.to_json(), 200

    # PUT /evaluacion/<id>
    def put(self, id):
        evaluacion = db.session.query(EvaluacionModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(evaluacion, key, value)
        db.session.add(evaluacion)
        db.session.commit()
        return evaluacion.to_json(), 200

    # DELETE /evaluacion/<id>
    def delete(self, id):
        evaluacion = db.session.query(EvaluacionModel).get_or_404(id)
        db.session.delete(evaluacion)
        db.session.commit()
        return {'message': 'Evaluación eliminada con éxito'}, 200

class Evaluaciones(Resource):
    # GET /evaluaciones
    def get(self):
        params = request.args
        query = db.session.query(EvaluacionModel)

        if 'fecha' in params:  # Verificar si se ha pasado un parámetro de búsqueda por fecha
            try:
                # Formato esperado en el filtro: dd/mm/yyyy
                fecha = datetime.strptime(params['fecha'], '%d/%m/%Y').date()  # Convertir string a date
                query = query.filter_by(fecha=fecha)
            except ValueError:  # Manejar el error de formato de fecha
                return {'message': 'Formato de fecha inválido. Use DD/MM/YYYY.'}, 400

        if 'descripcion' in params:
            descripcion = params.get('descripcion', '').strip()
            # FIltrar por cualquier coincidencia en la descripción
            query = query.filter(EvaluacionModel.descripcion.ilike(f"%{descripcion}%")) 

        evaluaciones = query.all() # "concatenar" los filtros y ejecutar la consulta
        return jsonify({'evaluaciones': [evaluacion.to_json() for evaluacion in evaluaciones]})

    # POST /evaluaciones
    def post(self):
        evaluacion = EvaluacionModel.from_json(request.get_json())
        db.session.add(evaluacion)
        db.session.commit()
        return evaluacion.to_json(), 201
