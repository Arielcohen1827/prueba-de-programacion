from .. import db

class Usuario(db.Model):
    id_usuario = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=False)
    contraseña = db.Column(db.String(100), nullable=False)
    rol = db.Column(db.String(50), nullable=False)

    # Relación con las notificaciones (1 a n)
    notificaciones = db.relationship("Notificacion", back_populates="usuario", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Usuario {self.email}>"

    # Convertir a JSON
    def to_json(self):
        usuario_json = {
            'id_usuario': self.id_usuario,
            'email': str(self.email),
            'contraseña': str(self.contraseña),
            'rol': str(self.rol)
        }

        return usuario_json
    
    def to_json_complete(self):
        notificaciones = [notificacion.to_json() for notificacion in self.notificaciones]
        usuario_json = {
            'id_usuario': self.id_usuario,
            'email': str(self.email),
            'contraseña': str(self.contraseña),
            'rol': str(self.rol),
            'notificaciones': notificaciones
        }
        return usuario_json
    
    @staticmethod
    def from_json(usuario_json):
        id_usuario = usuario_json.get('id_usuario')
        email = usuario_json.get('email')
        contraseña = usuario_json.get('contraseña')
        rol = usuario_json.get('rol')

        return Usuario(email=email, contraseña=contraseña, rol=rol)
