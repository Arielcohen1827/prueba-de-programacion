from .. import db

class Plan(db.Model):
    id_plan = db.Column(db.Integer, primary_key=True)
    id_ficha = db.Column(db.Integer, db.ForeignKey('ficha.id_ficha'), nullable=False)
    descripcion = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    # Relación con planes_ejercicios (1 a n)
    planes_ejercicios = db.relationship("PlanesEjercicios", back_populates="plan", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Plan {self.id_plan}>"

    # Convertir a JSON
    def to_json(self):
        plan_json = {
            'id_plan': self.id_plan,
            'id_ficha': self.id_ficha,
            'descripcion': str(self.descripcion),
            'estado': str(self.estado)
        }

        return plan_json
    
    def to_json_complete(self):
        planes_ejercicios = [plan_ejercicio.to_json() for plan_ejercicio in self.planes_ejercicios]
        plan_json = {
            'id_plan': self.id_plan,
            'id_ficha': self.id_ficha,
            'descripcion': str(self.descripcion),
            'estado': str(self.estado),
            'planes_ejercicios': planes_ejercicios
        }
        return plan_json
    
    @staticmethod
    def from_json(plan_json):
        id_plan = plan_json.get('id_plan')
        id_ficha = plan_json.get('id_ficha')
        descripcion = plan_json.get('descripcion')
        estado = plan_json.get('estado')

        return Plan(id_ficha=id_ficha, descripcion=descripcion, estado=estado)
