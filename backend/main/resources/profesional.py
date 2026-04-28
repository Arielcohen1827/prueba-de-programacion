from flask import request, jsonify
from flask_restful import Resource
from .. import db
from ..models.profesional import Profesional as ProfesionalModel

class Profesional(Resource):
    # GET /profesional/<id> - Obtener un profesional por ID
    def get(self, id):
        profesional = db.session.query(ProfesionalModel).get_or_404(id)
        return profesional.to_json(), 200

    # PUT /profesional/<id> - Actualizar un profesional
    def put(self, id):
        profesional = db.session.query(ProfesionalModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(profesional, key, value)
        db.session.add(profesional)
        db.session.commit()
        return profesional.to_json(), 200

    # DELETE /profesional/<id> - Eliminar un profesional
    def delete(self, id):
        profesional = db.session.query(ProfesionalModel).get_or_404(id)
        db.session.delete(profesional)
        db.session.commit()
        return {'message': 'Profesional eliminado con éxito'}, 200

class Profesionales(Resource):
    # GET /profesionales - Obtener todos los profesionales
    def get(self):
        params = request.args
        query = db.session.query(ProfesionalModel)
        if 'nombre' in params:
            nombre = params.get('nombre', '').strip()
            query = query.filter(ProfesionalModel.nombre.ilike(f"%{nombre}%"))
        if 'apellido' in params:
            apellido = params.get('apellido', '').strip()
            query = query.filter(ProfesionalModel.apellido.ilike(f"%{apellido}%"))
        if 'matricula' in params:
            matricula = params.get('matricula', '').strip()
            query = query.filter(ProfesionalModel.matricula.ilike(f"%{matricula}%"))
        if 'edad' in params:
            try:
                edad = int(params['edad'])
                query = query.filter(ProfesionalModel.edad == edad)
            except ValueError:
                return {"message": "Edad debe ser un número entero."}, 400
        return jsonify({'profesionales': [prof.to_json() for prof in query.all()]})

    # POST /profesionales - Crear un nuevo profesional
    def post(self):
        profesional = ProfesionalModel.from_json(request.get_json())
        db.session.add(profesional)
        db.session.commit()
        return profesional.to_json(), 201
