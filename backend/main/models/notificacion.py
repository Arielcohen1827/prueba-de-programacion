from .. import db
from datetime import datetime

class Notificacion(db.Model):
    id_notificacion = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuario.id_usuario'), nullable=False)
    mensaje = db.Column(db.Text, nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    leida = db.Column(db.Boolean, nullable=False, default=False)
    fecha = db.Column(db.Date, nullable=False)

    # Relación con el usuario (n a 1)
    usuario = db.relationship("Usuario", back_populates="notificaciones", uselist=False, single_parent=True)

    # Convertir a JSON
    def to_json(self):
        notificacion_json = {
            'id_notificacion': self.id_notificacion,
            'id_usuario': self.id_usuario,
            'mensaje': str(self.mensaje),
            'tipo': str(self.tipo),
            'leida': self.leida,
            'fecha': str(self.fecha)
        }

        return notificacion_json
    
    def to_json_short(self):
        notificacion_json = {
            'id_notificacion': self.id_notificacion,
            'mensaje': str(self.mensaje),
            'tipo': str(self.tipo),
            'leida': self.leida,
            'fecha': str(self.fecha)
        }

        return notificacion_json
    
    @staticmethod
    def from_json(notificacion_json):
        id_notificacion = notificacion_json.get('id_notificacion')
        id_usuario = notificacion_json.get('id_usuario')
        mensaje = notificacion_json.get('mensaje')
        tipo = notificacion_json.get('tipo')
        leida = notificacion_json.get('leida')
        fecha_str = notificacion_json.get('fecha')

        # Convertir la fecha de string a date
        try:
            # El json por default trae la fecha en formato yyyy-mm-dd
            fecha = datetime.strptime(fecha_str, '%Y-%m-%d').date() if fecha_str else None
        except ValueError:
            raise ValueError("Formato de fecha inválido. Use YYYY-MM-DD.")

        return Notificacion(id_usuario=id_usuario, mensaje=mensaje, tipo=tipo, leida=leida, fecha=fecha)
