from .. import db

class Paciente(db.Model):
    id_paciente = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    telefono = db.Column(db.String(20), nullable=False)

    # Relación con los turnos (1 a n)
    turnos = db.relationship("Turno", back_populates="paciente", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Paciente {self.nombre} {self.apellido}>"

    # Convertir a JSON
    def to_json(self):
        paciente_json = {
            'id_paciente': self.id_paciente,
            'id_usuario': self.id_usuario,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'edad': self.edad,
            'telefono': str(self.telefono)
        }

        return paciente_json
    
    def to_json_complete(self):
        turnos = [turno.to_json() for turno in self.turnos]
        paciente_json = {
            'id_paciente': self.id_paciente,
            'id_usuario': self.id_usuario,
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'edad': self.edad,
            'telefono': str(self.telefono),
            'turnos': turnos
        }

        return paciente_json
    
    @staticmethod
    def from_json(paciente_json):
        id_paciente = paciente_json.get('id_paciente')
        id_usuario = paciente_json.get('id_usuario')
        nombre = paciente_json.get('nombre')
        apellido = paciente_json.get('apellido')
        edad = paciente_json.get('edad')
        telefono = paciente_json.get('telefono')

        return Paciente(id_usuario=id_usuario, nombre=nombre, apellido=apellido, edad=edad, telefono=telefono)
