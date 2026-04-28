from .. import db
from datetime import datetime

class Turno(db.Model):
    id_turno = db.Column(db.Integer, primary_key=True)
    id_paciente = db.Column(db.Integer, db.ForeignKey('paciente.id_paciente'), nullable=False)
    id_profesional = db.Column(db.Integer, db.ForeignKey('profesional.id_profesional'), nullable=False)
    fecha = db.Column(db.Date, nullable=False)
    hora = db.Column(db.Time, nullable=False)
    estado = db.Column(db.String(50), nullable=False)

    # Relaciones con Paciente, Profesional y Plan (n a 1)
    paciente = db.relationship("Paciente", back_populates="turnos", uselist=False, single_parent=True)
    profesional = db.relationship("Profesional", back_populates="turnos", uselist=False, single_parent=True)

    # Convertir a JSON
    def to_json(self):
        
        turno_json = {
            'id_turno': self.id_turno,
            'id_paciente': self.id_paciente,
            'id_profesional': self.id_profesional,
            'fecha': str(self.fecha),
            'hora': str(self.hora),
            'estado': str(self.estado)
        }

        return turno_json
    
    def to_json_short(self):
        turno_json = {
            'id_turno': self.id_turno,
            'fecha': str(self.fecha),
            'hora': str(self.hora),
            'estado': str(self.estado)
        }

        return turno_json
    
    @staticmethod
    def from_json(turno_json):
        id_turno = turno_json.get('id_turno')
        id_paciente = turno_json.get('id_paciente')
        id_profesional = turno_json.get('id_profesional')
        fecha_str = turno_json.get('fecha')
        hora_str = turno_json.get('hora')
        estado = turno_json.get('estado')
        
        try:
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date() if fecha_str else None
            hora = datetime.strptime(hora_str, '%H:%M:%S').time() if hora_str else None
        except ValueError:
            raise ValueError("Formato de fecha u hora inválido. Use YYYY-MM-DD para fecha y HH:MM:SS para hora.")
        return Turno(id_paciente=id_paciente, id_profesional=id_profesional, fecha=fecha, hora=hora, estado=estado)
