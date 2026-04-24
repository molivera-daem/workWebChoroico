"""
@file core/__init__.py
@description Fábrica de aplicación (Application Factory) para inicializar Flask.
@author Miguel Olivera Labrin
"""

from flask import Flask
from config import Config

def create_app(config_class=Config):
    """
    Inicializa la aplicación Flask con la configuración dada.

    :param object config_class: Clase de configuración (Config, DevelopmentConfig, etc).
    :return: Instancia de la aplicación Flask.
    :rtype: Flask
    """
    app = Flask(__name__)
    app.config.from_object(config_class)

    from core.routes import main
    app.register_blueprint(main)

    return app
