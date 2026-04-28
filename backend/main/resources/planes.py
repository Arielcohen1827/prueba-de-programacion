from flask import request, jsonify
from flask_restful import Resource
from .. import db
from ..models.plan import Plan as PlanModel

class Plan(Resource):
    # GET /plan/<id> - Obtener un plan por ID
    def get(self, id):
        plan = db.session.query(PlanModel).get_or_404(id)
        return plan.to_json(), 200

    # PUT /plan/<id> - Actualizar un plan
    def put(self, id):
        plan = db.session.query(PlanModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(plan, key, value)
        db.session.add(plan)
        db.session.commit()
        return plan.to_json(), 200

    # DELETE /plan/<id> - Eliminar un plan
    def delete(self, id):
        plan = db.session.query(PlanModel).get_or_404(id)
        db.session.delete(plan)
        db.session.commit()
        return {'message': 'Plan eliminado con éxito'}, 200

class Planes(Resource):
    # GET /planes - Obtener todos los planes
    def get(self):
        params = request.args
        query = db.session.query(PlanModel)
        if 'descripcion' in params:
            descripcion = params.get('descripcion', '').strip()
            query = query.filter(PlanModel.descripcion.ilike(f"%{descripcion}%"))
        if 'estado' in params:
            estado = params.get('estado', '').strip()
            query = query.filter(PlanModel.estado.ilike(f"%{estado}%"))
        return jsonify({'planes': [plan.to_json() for plan in query.all()]})

    # POST /planes - Crear un nuevo plan
    def post(self):
        plan = PlanModel.from_json(request.get_json())
        db.session.add(plan)
        db.session.commit()
        return plan.to_json(), 201
