from flask import request, jsonify
from flask_restful import Resource
from .. import db
from ..models.ejercicio import Ejercicio as EjercicioModel

class Ejercicio(Resource):
    # GET /ejercicio/<id>
    def get(self, id):
        ejercicio = db.session.query(EjercicioModel).get_or_404(id)
        return ejercicio.to_json(), 200

    # PUT /ejercicio/<id>
    def put(self, id):
        ejercicio = db.session.query(EjercicioModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(ejercicio, key, value)
        db.session.add(ejercicio)
        db.session.commit()
        return ejercicio.to_json(), 200

    # DELETE /ejercicio/<id>
    def delete(self, id):
        ejercicio = db.session.query(EjercicioModel).get_or_404(id)
        db.session.delete(ejercicio)
        db.session.commit()
        return {'message': 'Ejercicio eliminado con éxito'}, 200

class Ejercicios(Resource):
    # GET /ejercicios
    def get(self):
        params = request.args
        if 'nombre' in params: # Verificar si se ha pasado un parámetro de búsqueda por nombre
            # Le agregué el ilike para que ignore mayusculas y minusculas
            ejercicios = db.session.query(EjercicioModel).filter(EjercicioModel.nombre.ilike(params['nombre'])).all()
        else:
            ejercicios = EjercicioModel.query.all()
        return jsonify({'ejercicios': [ejercicio.to_json() for ejercicio in ejercicios]})

    # POST /ejercicios
    def post(self):
        ejercicio = EjercicioModel.from_json(request.get_json())
        db.session.add(ejercicio)
        db.session.commit()
        return ejercicio.to_json(), 201
