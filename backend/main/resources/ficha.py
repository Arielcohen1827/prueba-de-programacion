from flask import request
from flask_restful import Resource

FICHAS = {
    1: {
        'paciente_id': 1,
        'diagnostico': 'Lumbalgia',
        'observaciones': 'Dolor leve al moverse',
        'estado': 'activo'
    },
    2: {
        'paciente_id': 2,
        'diagnostico': 'Esguince de tobillo',
        'observaciones': 'Inflamación moderada',
        'estado': 'activo'
    }
}


class Ficha(Resource):

    # GET /ficha/<id>
    def get(self, id):
        id = int(id)
        if id in FICHAS:
            return {"id": id, **FICHAS[id]}, 200
        return {"error": "La ficha no existe"}, 404

    # PUT /ficha/<id>
    def put(self, id):
        id = int(id)
        if id in FICHAS:
            data = request.get_json()

            if not data:
                return {"error": "No se enviaron datos"}, 400

            FICHAS[id].update(data)
            return {"message": "Ficha actualizada con éxito"}, 200

        return {"error": "La ficha no existe"}, 404

    # DELETE /ficha/<id>
    def delete(self, id):
        id = int(id)
        if id in FICHAS:
            del FICHAS[id]
            return {"message": "Ficha eliminada con éxito"}, 200

        return {"error": "La ficha no existe"}, 404


class Fichas(Resource):

    # GET /fichas
    def get(self):
        return [
            {"id": id, **ficha}
            for id, ficha in FICHAS.items()
        ], 200

    # POST /fichas
    def post(self):
        data = request.get_json()

        if not data:
            return {"error": "No se enviaron datos"}, 400

        # Validación mínima
        if "paciente_id" not in data or "diagnostico" not in data:
            return {"error": "Faltan campos obligatorios"}, 400

        new_id = max(FICHAS.keys()) + 1 if FICHAS else 1
        FICHAS[new_id] = data

        return {"id": new_id, **FICHAS[new_id]}, 201