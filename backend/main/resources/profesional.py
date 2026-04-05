from flask import request
from flask_restful import Resource

PROFESIONAL = {
    1: {'nombre': 'Manuel', 'edad': '25', 'profesion': 'Cardiologo'},
    2: {'nombre': 'Amparo', 'edad': '30',  'profesion': 'Dermatologa'}
}

class profecional(Resource):

    def get(self, id):
        if(int(id) in PROFESIONAL):
            return PROFESIONAL[int(id)], 200 
        return 'El profecional no existe', 404

    def put(self, id):
        if(int(id) in PROFESIONAL):
            data = request.get_json()
            profecional = PROFESIONAL[int(id)]
            profecional.update(data)
            return 'profecional actualizado con éxito', 200
        return 'El profecional no existe', 404
    
    def delete(self, id):
        if(int(id) in PROFESIONAL):
            del PROFESIONAL[int(id)]
            return 'profecional eliminado con éxito', 200
        return 'El profecional no existe', 404

class profecionales(Resource):

    def get(self):
        return PROFESIONAL, 200

    def post(self):
        profecional = request.get_json()
        id = int(max(PROFESIONAL.keys())) + 1
        PROFESIONAL[id] = profecional
        return PROFESIONAL[id], 201
