from .. import db

class Profesional(db.Model):
    id_profesional = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    matricula = db.Column(db.String(50), nullable=False)
    nombre = db.Column(db.String(100), nullable=False)
    apellido = db.Column(db.String(100), nullable=False)
    edad = db.Column(db.Integer, nullable=False)
    id_especialidad = db.Column(db.Integer, db.ForeignKey('especialidad.id_especialidad'), nullable=False)

    # Relación con los turnos (1 a n)
    turnos = db.relationship("Turno", back_populates="profesional", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Profesional {self.nombre} {self.apellido}>"

    # Convertir a JSON
    def to_json(self):
        profesional_json = {
            'id_profesional': self.id_profesional,
            'id_usuario': self.id_usuario,
            'matricula': str(self.matricula),
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'edad': self.edad,
            'id_especialidad': self.id_especialidad
        }

        return profesional_json
    
    def to_json_complete(self):
        turnos = [turno.to_json() for turno in self.turnos]
        profesional_json = {
            'id_profesional': self.id_profesional,
            'id_usuario': self.id_usuario,
            'matricula': str(self.matricula),
            'nombre': str(self.nombre),
            'apellido': str(self.apellido),
            'edad': self.edad,
            'id_especialidad': self.id_especialidad,
            'turnos': turnos
        }

        return profesional_json
    
    @staticmethod
    def from_json(profesional_json):
        id_profesional = profesional_json.get('id_profesional')
        id_usuario = profesional_json.get('id_usuario')
        matricula = profesional_json.get('matricula')
        nombre = profesional_json.get('nombre')
        apellido = profesional_json.get('apellido')
        edad = profesional_json.get('edad')
        id_especialidad = profesional_json.get('id_especialidad')

        return Profesional(id_usuario=id_usuario, matricula=matricula, nombre=nombre, apellido=apellido, edad=edad, id_especialidad=id_especialidad)
