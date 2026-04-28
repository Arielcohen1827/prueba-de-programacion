from .. import db

class Especialidad(db.Model):
    id_especialidad = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)

    # Convertir a JSON
    def to_json(self):
        especialidad_json = {
            'id_especialidad': self.id_especialidad,
            'nombre': str(self.nombre)
        }

        return especialidad_json
    
    @staticmethod # Método estático para crear una especialidad a partir de un JSON
    def from_json(especialidad_json):
        id_especialidad = especialidad_json.get('id_especialidad')
        nombre = especialidad_json.get('nombre')

        return Especialidad(nombre=nombre)
