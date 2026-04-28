from flask import request, jsonify
from flask_restful import Resource
from .. import db
from ..models.paciente import Paciente as PacienteModel

class Paciente(Resource):
    # GET /paciente/<id> - Obtener un paciente por ID
    def get(self, id):
        paciente = db.session.query(PacienteModel).get_or_404(id)
        return paciente.to_json(), 200

    # PUT /paciente/<id> - Actualizar un paciente
    def put(self, id):
        paciente = db.session.query(PacienteModel).get_or_404(id)
        data = request.get_json().items()
        for key, value in data:
            setattr(paciente, key, value)
        db.session.add(paciente)
        db.session.commit()
        return paciente.to_json(), 200

    # DELETE /paciente/<id> - Eliminar un paciente
    def delete(self, id):
        paciente = db.session.query(PacienteModel).get_or_404(id)
        db.session.delete(paciente)
        db.session.commit()
        return {'message': 'Paciente eliminado con éxito'}, 200

class Pacientes(Resource):
    # GET /pacientes - Obtener todos los pacientes
    def get(self):
        params = request.args
        query = db.session.query(PacienteModel)

        if 'nombre' in params:
            nombre = params.get('nombre', '').strip()
            query = query.filter(PacienteModel.nombre.ilike(f"%{nombre}%"))
        if 'apellido' in params:
            apellido = params.get('apellido', '').strip()
            query = query.filter(PacienteModel.apellido.ilike(f"%{apellido}%"))
        if 'edad' in params:
            try:
                edad = int(params['edad'])
                query = query.filter(PacienteModel.edad == edad)
            except ValueError:
                return {"message": "Edad debe ser un número entero."}, 400
        if 'telefono' in params:
            telefono = params.get('telefono', '').strip()
            query = query.filter(PacienteModel.telefono.ilike(f"%{telefono}%"))

        pacientes = query.all() # "concatenar" los filtros y ejecutar la consulta
        return jsonify({"pacientes": [paciente.to_json() for paciente in pacientes]})

    # POST /pacientes - Crear un nuevo paciente
    def post(self):
        paciente = PacienteModel.from_json(request.get_json())
        db.session.add(paciente)
        db.session.commit()
        return paciente.to_json(), 201
