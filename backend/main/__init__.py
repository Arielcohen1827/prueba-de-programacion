from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# Inicializar API
api = Api()

# Inicializar DB
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Import tardio para evitar importacion circular con db
    import main.resources as resources

    # Cargar variables de entorno (si existe .env)
    load_dotenv()

    # Configuración de base de datos (portable)
    db_path = os.getenv('DATABASE_PATH') or './DB/'
    db_name = os.getenv('DATABASE_NAME') or 'app.db'

    db_full_path = os.path.abspath(os.path.join(db_path, db_name))

    if not os.path.exists(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME')):
        os.mknod(os.getenv('DATABASE_PATH')+os.getenv('DATABASE_NAME'))

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_full_path

    # Inicializar DB
    db.init_app(app)

    # Rutas existentes
    api.add_resource(resources.pacienteResource, '/paciente/<int:id>')
    api.add_resource(resources.pacientesResource, '/pacientes')

    api.add_resource(resources.profesionalResource, '/profesional/<int:id>')
    api.add_resource(resources.profesionalesResource, '/profesionales')

    api.add_resource(resources.planResource, '/plan/<int:id>')
    api.add_resource(resources.planesResource, '/planes')

    api.add_resource(resources.fichaResource, '/ficha/<int:id>')
    api.add_resource(resources.fichasResource, '/fichas')

    api.add_resource(resources.notificaciones_pacienteResource, '/paciente/<int:paciente_id>/notificaciones')
    api.add_resource(resources.notificacionResource, '/notificacion/<int:id>')
    api.add_resource(resources.notificacionesResource, '/notificaciones')

    api.add_resource(resources.registerResource, '/register')
    api.add_resource(resources.loginResource, '/login')
    api.add_resource(resources.logoutResource, '/logout')

    # Nuevas rutas
    api.add_resource(resources.turnoResource, '/turno/<int:id>')
    api.add_resource(resources.turnosResource, '/turnos')

    api.add_resource(resources.evaluacionResource, '/evaluacion/<int:id>')
    api.add_resource(resources.evaluacionesResource, '/evaluaciones')

    api.add_resource(resources.ejercicioResource, '/ejercicio/<int:id>')
    api.add_resource(resources.ejerciciosResource, '/ejercicios')

    api.add_resource(resources.planEjercicioResource, '/plan_ejercicio/<int:id>')
    api.add_resource(resources.planesEjerciciosResource, '/planes_ejercicios')

    api.add_resource(resources.especialidadResource, '/especialidad/<int:id>')
    api.add_resource(resources.especialidadesResource, '/especialidades')

    # Inicializar API
    api.init_app(app)

    return app