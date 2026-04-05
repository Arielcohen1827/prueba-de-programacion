from flask import request
from flask_restful import Resource

PLANES = {
    1: {      
        'descripcion': 'Tratamiento para recuperación de rodilla',
        'ejercicios': ['Elongación de isquios', 'Sentadillas asistidas'], 
        'estado': 'Activo'          
    },
    2: {       
        'descripcion': 'Rehabilitación post-operatoria de hombro',
        'ejercicios': ['Rotacion externa con banda', 'Movilidad escapular'],
        'estado': 'Pendiente'
    }
}

class Plan(Resource):
    # GET: Obtener un plan de tratamiento
    def get(self, id):
        if int(id) in PLANES:
            return PLANES[int(id)], 200
        return 'El plan no existe', 404

    # PUT: Modificar un plan (o cancelar si eres USER)
    def put(self, id):
        if int(id) in PLANES:
            data = request.get_json()
            PLANES[int(id)].update(data)
            return 'Plan actualizado', 200
        return 'El plan no existe', 404

    # DELETE: Eliminar un plan
    def delete(self, id):
        if int(id) in PLANES:
            del PLANES[int(id)]
            return 'Plan eliminado', 200
        return 'El plan no existe', 404

class Planes(Resource):
    # GET: Obtener todos los planes 
    def get(self):
        return PLANES, 200

    # POST: Crear un plan de tratamiento
    def post(self):
        data = request.get_json()
        nuevo_id = int(max(PLANES.keys())) + 1 if PLANES else 1
        PLANES[nuevo_id] = data
        return PLANES[nuevo_id], 201
