from flask import request, jsonify
from flask_restful import Resource
from datetime import datetime
from .. import db
from ..models.ficha import Ficha as FichaModel

class Ficha(Resource):
    # GET /ficha/<id>
    def get(self, id):
        ficha = db.session.query(FichaModel).get_or_404(id)
        return ficha.to_json(), 200

    # PUT /ficha/<id>
    def put(self, id):
        ficha = db.session.query(FichaModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(ficha, key, value)
        db.session.add(ficha)
        db.session.commit()
        return ficha.to_json(), 200

    # DELETE /ficha/<id>
    def delete(self, id):
        ficha = db.session.query(FichaModel).get_or_404(id)
        db.session.delete(ficha)
        db.session.commit()
        return {'message': 'Ficha eliminada con éxito'}, 200

class Fichas(Resource):
    # GET /fichas
    def get(self):
        params = request.args
        query = db.session.query(FichaModel)

        if 'fecha_inicio' in params:
            try:
                fecha_inicio = datetime.strptime(params['fecha_inicio'], '%d/%m/%Y').date()
                query = query.filter(FichaModel.fecha_inicio >= fecha_inicio)
            except ValueError:
                return {"message": "Formato de fecha_inicio inválido. Use DD/MM/YYYY."}, 400
        if 'fecha_fin' in params:
            try:
                fecha_fin = datetime.strptime(params['fecha_fin'], '%d/%m/%Y').date()
                query = query.filter(FichaModel.fecha_fin <= fecha_fin)
            except ValueError:
                return {"message": "Formato de fecha_fin inválido. Use DD/MM/YYYY."}, 400
        if 'estado' in params:
            estado = params.get('estado', '').strip()
            query = query.filter(FichaModel.estado.ilike(f"%{estado}%"))
        if 'diagnostico' in params:
            diagnostico = params.get('diagnostico', '').strip()
            query = query.filter(FichaModel.diagnostico.ilike(f"%{diagnostico}%"))

        fichas = query.all() # "concatenar" los filtros y ejecutar la consulta
        
        return jsonify({"fichas": [ficha.to_json() for ficha in fichas]})

    # POST /fichas
    def post(self):
        ficha = FichaModel.from_json(request.get_json())
        db.session.add(ficha)
        db.session.commit()
        return ficha.to_json(), 201
