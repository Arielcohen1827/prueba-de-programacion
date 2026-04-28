from flask import request
from flask_restful import Resource

TURNOS = {
    1: {
        'paciente_id': 1,
        'fecha': '2026-07-01',
        'hora': '10:00',
        'profesional_id': 1,
        'estado': 'programado'
    },
    2: {
        'paciente_id': 2,
        'fecha': '2026-07-02',
        'hora': '14:00',
        'profesional_id': 1,
        'estado': 'programado'
    }
}

class Turno(Resource):
    
    # GET /turno/<id>
    def get(self, id):
        id = int(id)
        if id in TURNOS:
            return {"id": id, **TURNOS[id]}, 200
        return {"error": "El turno no existe"}, 404

    # PUT /turno/<id>
    def put(self, id):
        id = int(id)
        if id in TURNOS:
            data = request.get_json()

            if not data:
                return {"error": "No se enviaron datos"}, 400

            TURNOS[id].update(data)
            return {"message": "Turno actualizado con éxito"}, 200

        return {"error": "El turno no existe"}, 404

    # DELETE /turno/<id>
    def delete(self, id):
        id = int(id)
        if id in TURNOS:
            del TURNOS[id]
            return {"message": "Turno eliminado con éxito"}, 200

        return {"error": "El turno no existe"}, 404
    
class Turnos(Resource):

    # GET /turnos
    def get(self):
        return [
            {"id": id, **turno}
            for id, turno in TURNOS.items()
        ], 200
    
    # POST /turnos
    def post(self):
        data = request.get_json()

        if not data:
            return {"error": "No se enviaron datos"}, 400

        new_id = max(TURNOS.keys()) + 1 if TURNOS else 1
        TURNOS[new_id] = data
        return {"id": new_id, **data}, 201
