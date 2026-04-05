from flask import Flask
from dotenv import load_dotenv
from flask_restful import Api

import main.resources as resources

#inicializar restful
api = Api()

def create_app():
    # Inicializar app
    app = Flask(__name__)
    # Cargar variables de entorno
    load_dotenv()

    # Cargar recursos
    api.add_resource(resources.pacienteResource, '/paciente/<id>')
    api.add_resource(resources.pacientesResource, '/pacientes')
    api.add_resource(resources.profecionalResource, '/profecional/<id>')
    api.add_resource(resources.profecionalesResource, '/profecionales')
    api.add_resource(resources.planResource, '/plan/<id>')
    api.add_resource(resources.planesResource, '/planes')
    api.add_resource(resources.fichaResource, '/ficha/<id>')
    api.add_resource(resources.fichasResource, '/fichas')
    api.add_resource(resources.notificacionResource,'/notifaciones' )
    api.add_resource(resources.registerResource, '/register')
    api.add_resource(resources.loginResource, '/login')
    api.add_resource(resources.logoutResource,'/logout' )
    api.init_app(app)

    return app
