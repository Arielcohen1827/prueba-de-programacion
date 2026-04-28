from .. import db

class Ejercicio(db.Model):
    id_ejercicio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

    # Relación con planes_ejercicios (1 a n)
    planes_ejercicios = db.relationship("PlanesEjercicios", back_populates="ejercicio", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Ejercicio {self.nombre}>"

    # Convertir a JSON
    def to_json(self):
        ejercicio_json = {
            'id_ejercicio': self.id_ejercicio,
            'nombre': str(self.nombre),
            'descripcion': str(self.descripcion)
        }
        return ejercicio_json
    
    def to_json_complete(self):
        planes_ejercicios = [plan_ejercicio.to_json() for plan_ejercicio in self.planes_ejercicios]
        ejercicio_json = {
            'id_ejercicio': self.id_ejercicio,
            'nombre': str(self.nombre),
            'descripcion': str(self.descripcion),
            'planes_ejercicios': planes_ejercicios
        }
        return ejercicio_json
    
    @staticmethod # Método estático para crear un ejercicio a partir de un JSON
    def from_json(ejercicio_json):
        id_ejercicio = ejercicio_json.get('id_ejercicio')
        nombre = ejercicio_json.get('nombre')
        descripcion = ejercicio_json.get('descripcion')

        return Ejercicio(nombre=nombre, descripcion=descripcion) # El id no se incluye por ser autoincremental
