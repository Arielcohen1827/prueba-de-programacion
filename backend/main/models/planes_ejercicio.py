from .. import db

class PlanesEjercicios(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_plan = db.Column(db.Integer, db.ForeignKey('plan.id_plan'), nullable=False)
    id_ejercicio = db.Column(db.Integer, db.ForeignKey('ejercicio.id_ejercicio'), nullable=False)
    repeticiones = db.Column(db.Integer, nullable=False)
    series = db.Column(db.Integer, nullable=False)

    # Relaciones con Plan y Ejercicio (n a 1)
    ejercicio = db.relationship("Ejercicio", back_populates="planes_ejercicios", uselist=False, single_parent=True)
    plan = db.relationship("Plan", back_populates="planes_ejercicios", uselist=False, single_parent=True)

    # Convertir a JSON
    def to_json(self):
        pe_json = {
            'id': self.id,
            'id_plan': self.id_plan,
            'id_ejercicio': self.id_ejercicio,
            'repeticiones': self.repeticiones,
            'series': self.series
        }

        return pe_json
    
    def to_json_short(self):
        pe_json = {
            'id': self.id,
            'repeticiones': self.repeticiones,
            'series': self.series
        }

        return pe_json
    
    @staticmethod
    def from_json(pe_json):
        id = pe_json.get('id')
        id_plan = pe_json.get('id_plan')
        id_ejercicio = pe_json.get('id_ejercicio')
        repeticiones = pe_json.get('repeticiones')
        series = pe_json.get('series')

        return PlanesEjercicios(id_plan=id_plan, id_ejercicio=id_ejercicio, repeticiones=repeticiones, series=series)
