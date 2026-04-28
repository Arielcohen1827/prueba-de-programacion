from .. import db
from datetime import datetime

class Evaluacion(db.Model):
    id_evaluacion = db.Column(db.Integer, primary_key=True)
    id_ficha = db.Column(db.Integer, db.ForeignKey('ficha.id_ficha'), nullable=False)
    id_profesional = db.Column(db.Integer, db.ForeignKey('profesional.id_profesional'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    descripcion = db.Column(db.Text, nullable=False)

    # Convertir a JSON
    def to_json(self):
        evaluacion_json = {
            'id_evaluacion': self.id_evaluacion,
            'id_ficha': self.id_ficha,
            'id_profesional': self.id_profesional,
            'fecha': str(self.fecha),
            'descripcion': str(self.descripcion)
        }

        return evaluacion_json
    
    @staticmethod # Método estático para crear una evaluación a partir de un JSON
    def from_json(evaluacion_json):
        id_evaluacion = evaluacion_json.get('id_evaluacion')
        id_ficha = evaluacion_json.get('id_ficha')
        id_profesional = evaluacion_json.get('id_profesional')
        fecha_str = evaluacion_json.get('fecha')
        descripcion = evaluacion_json.get('descripcion')

        # Convertir la fecha de string a date
        try:
            # El json por default trae la fecha en formato yyyy-mm-dd
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date() if fecha_str else None
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")

        return Evaluacion(id_ficha=id_ficha, id_profesional=id_profesional, fecha=fecha, descripcion=descripcion)
