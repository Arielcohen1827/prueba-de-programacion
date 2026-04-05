from flask import request
from flask_restful import Resource

PACIENTES = {
    1: {'nombre': 'Pepe', 'edad': '25'},
    2: {'nombre': 'Juana', 'edad': '30'}
}

class Paciente(Resource):

    # GET/paciente/id para ver uno en particular
    def get(self, id):
        if(int(id) in PACIENTES):
            return PACIENTES[int(id)], 200 # Retorna con status http
        return 'El Profecial no existe', 404

    def put(self, id):
        if(int(id) in PACIENTES):
            data = request.get_json() # Se toma del body de la request en formato json
            paciente = PACIENTES[int(id)]
            paciente.update(data)
            return 'paciente actualizado con éxito', 200
        return 'El paciente no existe', 404
    
    def delete(self, id):
        if(int(id) in PACIENTES):
            del PACIENTES[int(id)]
            return 'paciente eliminado con éxito', 200
        return 'El paciente no existe', 404

class Pacientes(Resource):

    # GET/PACIENTES para ver todos los pacientes
    def get(self):
        return PACIENTES, 200

    def post(self):
        paciente = request.get_json()
        id = int(max(PACIENTES.keys())) + 1
        PACIENTES[id] = paciente
        return PACIENTES[id], 201 # Status code para creación exitosa
