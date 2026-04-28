from flask import request, jsonify
from flask_restful import Resource
from .. import db
from ..models.planes_ejercicio import PlanesEjercicios as PlanesEjerciciosModel

class PlanEjercicio(Resource):
    # GET /plan_ejercicio/<id>
    def get(self, id):
        plan_ejercicio = db.session.query(PlanesEjerciciosModel).get_or_404(id)
        return plan_ejercicio.to_json(), 200

    # PUT /plan_ejercicio/<id>
    def put(self, id):
        planEjercicio = db.session.query(PlanesEjerciciosModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(planEjercicio, key, value)
        db.session.add(planEjercicio)
        db.session.commit()
        return planEjercicio.to_json(), 200

    # DELETE /plan_ejercicio/<id>
    def delete(self, id):
        plan_ejercicio = db.session.query(PlanesEjerciciosModel).get_or_404(id)
        db.session.delete(plan_ejercicio)
        db.session.commit()
        return {'message': 'PlanEjercicio eliminado con éxito'}, 200

class PlanesEjercicios(Resource):
    # GET /planes_ejercicios
    def get(self):
        params = request.args
        query = db.session.query(PlanesEjerciciosModel)

        # FIltrar por series y repeticiones
        if 'repeticiones' in params:
            repeticiones = params.get('repeticiones', '').strip()
            query = query.filter(PlanesEjerciciosModel.repeticiones == repeticiones)
        if 'series' in params:
            series = params.get('series', '').strip()
            query = query.filter(PlanesEjerciciosModel.series == series)

        planes_ejercicios = query.all() # "concatenar" los filtros y ejecutar la consulta
        return jsonify({"planes_ejercicios": [pe.to_json() for pe in planes_ejercicios]})

    # POST /planes_ejercicios
    def post(self):
        plan_ejercicio = PlanesEjerciciosModel.from_json(request.get_json())
        db.session.add(plan_ejercicio)
        db.session.commit()
        return plan_ejercicio.to_json(), 201
