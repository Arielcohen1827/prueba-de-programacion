from datetime import datetime
from .. import db

class Ficha(db.Model):
    id_ficha = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    diagnostico = db.Column(db.Text, nullable=False)
    estado = db.Column(db.String(50), nullable=False)
    fecha_inicio = db.Column(db.Date, nullable=False)
    fecha_fin = db.Column(db.Date, nullable=True)

    # Convertir a JSON
    def to_json(self):
        ficha_json = {
            'id_ficha': self.id_ficha,
            'id_paciente': self.id_paciente,
            'diagnostico': str(self.diagnostico),
            'estado': str(self.estado),
            'fecha_inicio': str(self.fecha_inicio),
            'fecha_fin': str(self.fecha_fin) if self.fecha_fin else None
        }

        return ficha_json
    
    @staticmethod # Método estático para crear una ficha a partir de un JSON
    def from_json(ficha_json):
        id_ficha = ficha_json.get('id_ficha')
        id_paciente = ficha_json.get('id_paciente')
        diagnostico = ficha_json.get('diagnostico')
        estado = ficha_json.get('estado')
        fecha_inicio_str = ficha_json.get('fecha_inicio')
        fecha_fin_str = ficha_json.get('fecha_fin')

        # Convertir las fechas de string a date
        try:
            fecha_inicio = datetime.strptime(fecha_inicio_str, '%Y-%m-%d').date() if fecha_inicio_str else None
            fecha_fin = datetime.strptime(fecha_fin_str, '%Y-%m-%d').date() if fecha_fin_str else None
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")

        return Ficha(id_paciente=id_paciente, diagnostico=diagnostico, estado=estado, fecha_inicio=fecha_inicio, fecha_fin=fecha_fin)
