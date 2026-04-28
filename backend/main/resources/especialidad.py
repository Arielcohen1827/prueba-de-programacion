from flask import request, jsonify
from flask_restful import Resource
from .. import db
from ..models.especialidad import Especialidad as EspecialidadModel

class Especialidad(Resource):
    # GET /especialidad/<id>
    def get(self, id):
        especialidad = db.session.query(EspecialidadModel).get_or_404(id)
        return especialidad.to_json(), 200

    # PUT /especialidad/<id>
    def put(self, id):
        especialidad = db.session.query(EspecialidadModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(especialidad, key, value)
        db.session.add(especialidad)
        db.session.commit()
        return especialidad.to_json(), 200

    # DELETE /especialidad/<id>
    def delete(self, id):
        especialidad = db.session.query(EspecialidadModel).get_or_404(id)
        db.session.delete(especialidad)
        db.session.commit()
        return {'message': 'Especialidad eliminada con éxito'}, 200

class Especialidades(Resource):
    # GET /especialidades
    def get(self):
        params = request.args
        if 'nombre' in params: # Verificar si se ha pasado un parámetro de búsqueda por nombre
            # Le agregué el ilike para que ignore mayusculas y minusculas
            especialidades = db.session.query(EspecialidadModel).filter(EspecialidadModel.nombre.ilike(params['nombre'])).all()
        else:
            especialidades = EspecialidadModel.query.all()
        return jsonify({'especialidades': [espec.to_json() for espec in especialidades]})

    # POST /especialidades
    def post(self):
        especialidad = EspecialidadModel.from_json(request.get_json())
        db.session.add(especialidad)
        db.session.commit()
        return especialidad.to_json(), 201
